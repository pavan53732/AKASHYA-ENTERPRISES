// Units: INR, metric tonnes, hours, moisture fractions. Not a guaranteed plant forecast.
function calculate(x){
 const finite=n=>typeof n==="number"&&Number.isFinite(n), positive=n=>finite(n)&&n>0;
 if(!positive(x.days)||x.days>31||!positive(x.hours)||x.hours>24||!positive(x.availability)||x.availability>1||!finite(x.moisture)||x.moisture<0||x.moisture>=1||!finite(x.finishedMoisture)||x.finishedMoisture<0||x.finishedMoisture>=1||!finite(x.loss)||x.loss<0||x.loss>=1||!positive(x.target))throw Error("Invalid scenario inputs");
 // Existing repository convention: rejected solids are dry-only; allocate them after drying. Real loss moisture must be measured.
 const hours=x.days*x.hours*x.availability, solids=(1-x.finishedMoisture)/(1-x.loss), wet=solids/(1-x.moisture), dry=solids+x.finishedMoisture, water=wet-dry;
 if(water< -1e-9)throw Error("Incoming feed too dry for this drying-only model");
 const capacity=n=>finite(n)&&n>=0?n:null;
 const wetLimit=capacity(x.wetTPH), dryLimit=capacity(x.dryTPH), evaporationLimit=capacity(x.evapTPH);
 const limits={wet:wetLimit===null?null:wetLimit/wet,dry:dryLimit===null?null:dryLimit/dry,evap:water<=0?Infinity:evaporationLimit===null?null:evaporationLimit/water,press:capacity(x.pressTPH),transfer:capacity(x.transferSaleableTPH)};
 const unsupported=finite(x.moistureLimit)&&(x.strictLimit?x.moisture>=x.moistureLimit:x.moisture>x.moistureLimit);
 const missing=Object.keys(limits).filter(k=>limits[k]===null);
 if(!finite(x.moistureLimit))missing.push("moisture limit");
 const known=Object.values(limits).filter(n=>n!==null&&Number.isFinite(n));
 const stopped=known.includes(0);
 const bound=stopped?0:unsupported||!known.length?null:Math.min(x.target,hours*Math.min(...known));
 const out={hours,wetPerT:wet,dryPerT:dry,waterPerT:Math.max(0,water),dryerOutletMoisture:x.finishedMoisture/dry,requiredWetTPH:x.target*wet/hours,requiredDryTPH:x.target*dry/hours,requiredEvapTPH:x.target*Math.max(0,water)/hours,requiredPressTPH:x.target/hours,status:stopped?"SHUTDOWN: ZERO REQUIRED STAGE CAPACITY":unsupported?"OUTSIDE MOISTURE RATING":missing.length?"CONDITIONAL UPPER BOUND; MISSING STAGES":"ILLUSTRATIVE INPUTS; NOT GUARANTEE",missing,boundT:bound,qualified:false};
 const keys=["woodPrice","salePrice","kwhPerT","tariff","fuelKgPerWaterT","fuelPricePerKg","variableOtherPerT","fixedMonthly","capex","workingCapital"];
 if(bound===null||unsupported||(!stopped&&missing.length)||keys.some(k=>!finite(x[k])||x[k]<0)){out.financeStatus="UNKNOWN: insufficient capacity or cost evidence";return out}
 const revenue=bound*x.salePrice, wood=bound*wet*x.woodPrice, electricity=bound*x.kwhPerT*x.tariff, fuel=bound*Math.max(0,water)*x.fuelKgPerWaterT*x.fuelPricePerKg, other=bound*x.variableOtherPerT, opex=wood+electricity+fuel+other+x.fixedMonthly;
 return {...out,revenue,wood,electricity,fuel,other,opex,ebitda:revenue-opex,initialCash:x.capex+x.workingCapital,financeStatus:"ILLUSTRATIVE ONLY; excludes finance, tax and WC changes"};
}

function longHorizon(x,esc){
 const rates=["sale","wood","power","fuel","other","fixed"];if(rates.some(k=>!Number.isFinite(esc[k])||esc[k]<=-1)||!Array.isArray(esc.utilisation)||esc.utilisation.length!==15||esc.utilisation.some(u=>!Number.isFinite(u)||u<0||u>1))throw Error("Invalid 15-year inputs");
 let cash=-(x.capex+x.workingCapital);
 return esc.utilisation.map((u,i)=>{const year=i+1,fixed=x.fixedMonthly*(1+esc.fixed)**i,r=calculate({...x,salePrice:x.salePrice*(1+esc.sale)**i,woodPrice:x.woodPrice*(1+esc.wood)**i,tariff:x.tariff*(1+esc.power)**i,fuelPricePerKg:x.fuelPricePerKg*(1+esc.fuel)**i,variableOtherPerT:x.variableOtherPerT*(1+esc.other)**i,fixedMonthly:fixed});
 if(r.ebitda===undefined)return {year,status:r.status+" / no financial forecast"};
 const revenue=12*r.revenue*u,opex=12*((r.opex-fixed)*u+fixed),ebitda=revenue-opex,replacement=esc.replacement?.[year]??0;if(!Number.isFinite(replacement)||replacement<0)throw Error("Invalid replacement cost");cash+=ebitda-replacement;return {year,tonnes:12*r.boundT*u,revenue,opex,ebitda,replacement,cumulativeUnleveredCash:cash,status:r.status};});
}

export {calculate,longHorizon};
