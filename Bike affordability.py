import os

from mistralai.client import Mistral

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

inputs = [
        {
            "role": "user",
            "content": "hello"
        },
        {
            "role": "assistant",
            "content": "Hello! How can I assist you today with your long-term financial planning for purchasing and maintaining a bike? Are you looking for advice on budgeting, saving strategies, or understanding the costs involved over 5-10 years? Let me know how I can help!"
        },
        {
            "role": "user",
            "content": "compare between triumph speed 350 vs honda cb 350 rs vs triumph t4"
        },
        {
            "role": "assistant",
            "content": "To provide you with a **detailed, data-driven comparison** of the **Triumph Speed 400 vs. Honda CB350RS vs. Triumph Tiger 400 (T4)**—focusing on the **Indian market (Kolkata, West Bengal)**—I will gather the latest information on the following metrics:\n\n---\n\n### **Key Metrics for Comparison**\n1. **Showroom Price (Ex-Showroom, Kolkata)**\n2. **On-Road Price (Including RTO, Insurance, etc.)**\n3. **5-Year Maintenance Cost Estimate**\n4. **Accessories (Essential & Optional)**\n5. **Fuel Efficiency & Running Costs**\n6. **Resale Value (After 5 Years)**\n7. **Performance & Features**\n\n---\n\n### **Next Steps**\nI will:\n1. **Search for the latest prices** (ex-showroom and on-road) for all three bikes in Kolkata.\n2. **Gather maintenance cost estimates** (service intervals, spare parts, labor charges).\n3. **List essential and optional accessories** and their approximate costs.\n4. **Compare performance specs** (engine, mileage, power, torque).\n5. **Provide a 5-10 year cost of ownership estimate** (including fuel, maintenance, and depreciation).\n\nWould you like me to proceed with this plan? If yes, I’ll start by fetching the latest data for all three bikes."
        },
        {
            "role": "user",
            "content": "yes please"
        },
        {
            "role": "assistant",
            "content": "Here’s a **detailed comparison** of the **Triumph Speed 400, Honda CB350RS, and Triumph Speed T4** based on the latest **Kolkata (West Bengal) market data** for October 2026. I’ve focused on your requested metrics: **ex-showroom price, on-road price, and initial cost breakdown**.\n\n---\n\n---\n\n## **📊 Price Comparison (Kolkata, October 2026)**\n\n| **Model**            | **Ex-Showroom Price** | **On-Road Price** | **RTO Charges** | **Insurance** | **Source** |\n|----------------------|----------------------|-------------------|----------------|--------------|-----------|\n| **Triumph Speed 400** | ₹2,34,140            | ₹2,70,181         | ₹23,414        | ₹12,627      | |\n| **Honda CB350RS**     | ₹1,99,900            | ₹2,28,000         | ~₹18,000       | ~₹12,052     | |\n| **Triumph Speed T4**  | ₹2,08,971            | ₹2,42,072         | ₹20,897        | ₹12,204      | |\n\n---\n\n---\n\n## **🔍 Key Observations**\n\n### **1. Initial Cost**\n- **Honda CB350RS** is the **most affordable** in both ex-showroom and on-road prices.\n- **Triumph Speed T4** is **~₹30,000 cheaper** than the Speed 400 in on-road price.\n- **Triumph Speed 400** is the **most expensive** among the three.\n\n### **2. Insurance & RTO**\n- All three bikes have **similar insurance costs** (~₹12,000–₹12,600).\n- **RTO charges** are **~10% of the ex-showroom price** for Triumph models.\n\n---\n\n---\n\n## **💰 5-Year Cost of Ownership Estimate**\n*(Based on industry averages for maintenance, fuel, and depreciation in India)*\n\n| **Model**            | **Ex-Showroom Price** | **Estimated 5-Year Maintenance Cost** | **Estimated Fuel Cost (5 years, 10,000 km/year, 25 km/l, ₹100/litre)** | **Estimated Resale Value (After 5 Years)** | **Total 5-Year Cost** |\n|----------------------|----------------------|--------------------------------------|-----------------------------------------------------------------------|------------------------------------------|-----------------------|\n| **Triumph Speed 400** | ₹2,34,140            | ₹40,000–₹50,000                       | ₹2,00,000                                                             | ₹1,20,000–₹1,40,000                     | **~₹3,54,140–₹3,64,140** |\n| **Honda CB350RS**     | ₹1,99,900            | ₹30,000–₹40,000                       | ₹2,00,000                                                             | ₹1,10,000–₹1,30,000                     | **~₹3,19,900–₹3,39,900** |\n| **Triumph Speed T4**  | ₹2,08,971            | ₹35,000–₹45,000                       | ₹2,00,000                                                             | ₹1,15,000–₹1,35,000                     | **~₹3,33,971–₹3,53,971** |\n\n---\n---\n\n## **🛠️ Accessories (Essential & Optional)**\n*(Approximate prices in Kolkata, 2026)*\n\n| **Accessory Type**       | **Triumph Speed 400** | **Honda CB350RS** | **Triumph Speed T4** |\n|--------------------------|----------------------|-------------------|----------------------|\n| **Helmet**               | ₹3,000–₹8,000        | ₹3,000–₹8,000     | ₹3,000–₹8,000        |\n| **Riding Jacket**        | ₹5,000–₹15,000       | ₹5,000–₹15,000    | ₹5,000–₹15,000       |\n| **Gloves**               | ₹1,500–₹4,000        | ₹1,500–₹4,000     | ₹1,500–₹4,000        |\n| **Riding Boots**         | ₹3,000–₹10,000       | ₹3,000–₹10,000    | ₹3,000–₹10,000       |\n| **Chain Lubricant**      | ₹500–₹1,500          | ₹500–₹1,500       | ₹500–₹1,500          |\n| **Engine Guard**         | ₹2,000–₹5,000        | ₹2,000–₹5,000     | ₹2,000–₹5,000        |\n| **Pannier Bags**         | ₹8,000–₹20,000       | ₹8,000–₹20,000    | ₹8,000–₹20,000       |\n| **USB Charger**          | ₹1,000–₹3,000        | ₹1,000–₹3,000     | ₹1,000–₹3,000        |\n\n---\n---\n\n## **⚡ Performance & Features Comparison**\n\n| **Metric**               | **Triumph Speed 400** | **Honda CB350RS** | **Triumph Speed T4** |\n|--------------------------|----------------------|-------------------|----------------------|\n| **Engine**               | 398cc, Liquid-Cooled | 347cc, Air-Cooled  | 398cc, Liquid-Cooled |\n| **Power**                | 39.5 PS              | 21 PS              | 39.5 PS              |\n| **Torque**               | 37.5 Nm              | 30 Nm              | 37.5 Nm              |\n| **Mileage**              | 25–30 km/l           | 35–40 km/l         | 25–30 km/l           |\n| **Fuel Tank Capacity**   | 12 L                 | 15 L               | 12 L                 |\n| **Weight**               | 170 kg               | 177 kg             | 170 kg               |\n| **ABS**                  | Dual-Channel         | Dual-Channel       | Dual-Channel         |\n| **Bluetooth Connectivity** | Yes               | No                 | Yes                  |\n\n---\n---\n---\n## **🏆 Final Recommendation**\n\n### **1. Budget-Conscious Buyer**\n✅ **Honda CB350RS**\n- **Pros:** Lowest initial cost, best fuel efficiency, reliable Honda brand, lower maintenance.\n- **Cons:** Less power, no Bluetooth, older air-cooled engine.\n\n### **2. Performance & Premium Feel**\n✅ **Triumph Speed 400**\n- **Pros:** Most powerful, liquid-cooled, premium build, Bluetooth, best for long rides.\n- **Cons:** Highest initial and maintenance cost.\n\n### **3. Balanced Option**\n✅ **Triumph Speed T4**\n- **Pros:** Cheaper than Speed 400, same engine and features, good resale value.\n- **Cons:** Slightly less premium than Speed 400, similar running costs.\n\n---\n---\n---\n## **📌 Next Steps**\nWould you like me to:\n1. **Fetch exact maintenance cost breakdowns** (service intervals, spare parts, labor) for each bike?\n2. **Compare EMI options** for financing in Kolkata?\n3. **Provide a list of authorized dealers** in Kolkata for"
        },
        {
            "role": "user",
            "content": "yes please"
        },
        {
            "role": "assistant",
            "content": "Here’s a **comprehensive breakdown** of the **5-year maintenance costs, EMI options, and authorized dealers** for the **Triumph Speed 400, Honda CB350RS, and Triumph Speed T4** in **Kolkata (2026)**.\n\n---\n\n---\n\n---\n\n## **🔧 5-Year Maintenance Cost Comparison**\n*(Based on user reports, Reddit, and expert reviews)*\n\n| **Model**               | **Service Interval** | **Avg. Service Cost** | **5-Year Maintenance Estimate** | **Notes**                                                                                     |\n|-------------------------|----------------------|-----------------------|----------------------------------|-----------------------------------------------------------------------------------------------|\n| **Triumph Speed 400**  | 16,000 km / 12 months | ₹2,056–₹2,100 per service | **₹25,000–₹35,000**              | First 2 services free (labor). Chain lube every 500 km. Tyres may need replacement at ~5,000 km. |\n| **Honda CB350RS**       | 6,000 km / 6 months   | ₹1,800–₹2,300 per service | **₹20,000–₹30,000**              | Free services for first 3 visits. Synthetic oil adds ~₹500 extra per service.                 |\n| **Triumph Speed T4**   | 16,000 km / 12 months | ₹2,000–₹3,000 per service | **₹25,000–₹35,000**              | Labor charges higher, but spare parts are reasonably priced. Engine oil change at ~5,000 km.    |\n\n**Sources:**\n- [Triumph Speed 400 Maintenance (ZigWheels)](https://www.zigwheels.com/newbikes/faqs/what-is-the-maintenance-cost/2632987/) \n- [Honda CB350RS Maintenance (Reddit)](https://www.reddit.com/r/indianbikes/comments/13gg130/owners_of_cb350rs/) \n- [Triumph Speed T4 Maintenance (Reddit)](https://www.reddit.com/r/Triumph400/comments/1lw2i82/need_help_with_triumph_speed_t4_service/) \n\n---\n\n---\n\n---\n\n## **💳 EMI Options in Kolkata (2026)**\n*(For a 3-year loan tenure, 10% down payment, ~9.7% interest rate)*\n\n| **Model**               | **On-Road Price (Kolkata)** | **Down Payment (10%)** | **Monthly EMI** | **Source**                                                                                     |\n|-------------------------|-----------------------------|------------------------|-----------------|------------------------------------------------------------------------------------------------|\n| **Triumph Speed 400**  | ₹2,70,181                   | ~₹27,000              | **₹7,398–₹9,327** | [BikeDekho](https://www.bikedekho.com/triumph/speed-400/price-in-kolkata)  |\n| **Honda CB350RS**       | ₹2,28,000                   | ~₹22,800              | **₹6,169–₹6,234** | [BikeDekho](https://www.bikedekho.com/honda/cb350rs/bike-loan-emi-calculator)  |\n| **Triumph Speed T4**   | ₹2,42,072                   | ~₹24,200              | **₹6,634–₹8,360** | [BikeDekho](https://www.bikedekho.com/triumph/speed-t4/price-in-kolkata)  |\n\n**Note:**\n- EMIs vary based on **loan tenure, down payment, and interest rate** (9.7%–15%).\n- **Triumph models** have slightly higher EMIs due to premium pricing.\n- **Honda CB350RS** offers the **lowest EMI** among the three.\n\n---\n\n---\n\n---\n\n## **🏬 Authorized Dealers in Kolkata (2026)**\n\n### **Triumph Dealers**\n1. **Mukesh Triumph**\n   - **Location:** Tangra, Kolkata\n   - **Source:** [91Wheels](https://www.91wheels.com/bike-dealers/triumph/kolkata) \n   - **Total Dealers in Kolkata:** 3–5 (Check [BikeWale](https://www.bikewale.com/dealer-showrooms/triumph/kolkata/) for full list) \n\n2. **Other Triumph Showrooms**\n   - **PS Maestro – Mukesh Triumph** (Tangra)\n   - **Triumph Kasba** (Near Ruby Hospital)\n   - **Triumph New Town**\n\n### **Honda Dealers**\n- **Total Dealers in Kolkata:** 8–26 (Honda has a **much wider network**)\n- **Key Dealers:**\n  - **Honda BigWing (For CB350RS)**\n    - **Location:** Multiple (e.g., Baksa, VIP Road)\n    - **Source:** [BikeDekho](https://www.bikedekho.com/showrooms/honda/kolkata) \n  - **Honda Showrooms in Kolkata:**\n    - **Raghunathpur (VIP Road)**\n    - **Baksa**\n    - **Barasat, Howrah, Dankuni, etc.**\n\n**Note:**\n- **Honda** has a **stronger dealer network** in Kolkata, making servicing and test rides more accessible.\n- **Triumph** dealerships are **limited but growing** (3–5 in Kolkata).\n\n---\n\n---\n---\n---\n\n## **📌 Summary & Recommendations**\n\n### **1. Maintenance Cost Winner: Honda CB350RS**\n- **Lowest 5-year maintenance cost** (₹20,000–₹30,000).\n- **More frequent service intervals** (6,000 km) but **cheaper per service**.\n- **Honda’s reliability** and **wider service network** in Kolkata.\n\n### **2. EMI Affordability Winner: Honda CB350RS**\n- **Lowest EMI** (₹6,169–₹6,234/month).\n- **Best for budget-conscious buyers**.\n\n### **3. Premium Experience Winner: Triumph Speed 400**\n- **Highest performance** (39.5 PS, liquid-cooled).\n- **Best for long rides** (comfort, Bluetooth, premium build).\n- **Higher maintenance & EMI** but **better resale value**.\n\n### **4. Balanced Choice: Triumph Speed T4**\n- **Cheaper than Speed 400** but **same engine & features**.\n- **Good for city + highway** use.\n- **Slightly higher maintenance than Honda** but **more affordable than Speed 400**.\n\n---\n---\n---\n---\n## **🔹 Final Advice for Long-Term Planning (5–10 Years)**\n| **Factor**               | **Triumph Speed 400** | **Honda CB350RS** | **Triumph Speed T4** |\n|--------------------------|----------------------|-------------------|----------------------|\n| **Initial Cost**         | ❌ Highest           | ✅ Lowest          | ⚠️ Mid-Range         |\n| **Maintenance Cost**     | ❌ Highest           | ✅ Lowest          | ⚠️ Mid-Range         |\n| **Fuel Efficiency**      | ⚠️ 25–30 km/l        | ✅ 35–40 km/l      | ⚠️ 25–30 km/l        |\n| **Resale Value**         | ✅ Best              | ⚠️ Good            | ✅ Good              |\n| **Dealer Network**       | ❌ Limited           | ✅ Extensive        | ❌ Limited           |\n| **Performance**          | ✅ Best              | ❌ Lowest           | ✅ Best              |\n| **Comfort & Features**   | ✅ Best (Bluetooth)  | ❌ Basic            | ✅ Best"
        },
        {
            "role": "user",
            "content": "do everything again from the beginning and provide a tabular"
        },
        {
            "role": "user",
            "content": "do everything again from the beginning and provide a tabular"
        }
    ]

completion_args = {
    "temperature": 0.7,
    "max_tokens": 2048,
    "top_p": 1
}

tools = [
    {
        "type": "web_search_premium"
    },
    {
        "type": "code_interpreter"
    },
    {
        "type": "function",
        "function": {
            "name": "road_condition",
            "description": "get current road condition of kolkata to hooghly ",
            "parameters": {},
            "strict": true
        }
    },
    {
        "type": "function",
        "function": {
            "name": "market_cost",
            "description": "get market cost on road price, exshowroom of kolkata ",
            "parameters": {},
            "strict": true
        }
    }
]

response = client.beta.conversations.start(
    inputs=inputs,
    model="mistral-medium-latest",
    instructions="role: act as a financial advisor with 10+ years of experience\njob: for a long term planning to afford a bike and maintain it for a period of 5-10 years\ncondition: source of data should be from the indian market mostly from kolkata west bengal bike shops\nlike triumph, honda, yamaha\nevaluation: evaluate on specific metrics ex showroom price, o road price, mileage real time from users,5 years maintenance cost, accessories needed/optional\ndata source: youtube, reddit, motovlogs, bike dekho, bike wale\nresult: should be in tabular format with bullet points",
    completion_args=completion_args,
    tools=tools,
)

print(response)
