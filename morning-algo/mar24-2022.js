/*
  Given an array of ailments (illnesses), and an array of medication objects that have a nested array of treatedSymptoms
  return the medication name(s) that treats the most given symptoms
*/

const medications = [
    {
        name: "Sulforaphane",
        treatableSymptoms: [
            "dementia",
            "alzheimer's",
            "inflammation",
            "neuropathy",
        ],
    },
    {

        name: "Longvida Curcumin",
        treatableSymptoms: [
            "pain",
            "inflammation",
            "depression",
            "arthritis",
            "anxiety",
        ],
    },
    {
        name: "Hericium erinaceus",
        treatableSymptoms: [
            "anxiety",
            "cognitive decline",
            "depression"],
    },
    {
        name: "Nicotinamide mononucleotide",
        treatableSymptoms: [
            "ageing",
            "low NAD",
            "obesity",
            "mitochondrial myopathy",
            "diabetes",
        ],
    },
    {
        name: "PainAssassinator",
        treatableSymptoms: [
            "pain",
            "inflammation",
            "cramps",
            "headache",
            "toothache",
            "back pain",
            "fever",
        ],
    },
];


/*
Input: ["pain"], medications
Output: ["PainAssassinator", "Longvida Curcumin"]
*/

/*
Input: ["pain", "inflammation", "depression"], medications
Output: ["Longvida Curcumin"]
*/

/*
Input: ["existential dread"], medications
Output: []
*/

/*
output array
counter on how many symptoms it has treated
if a new medication treats more, make a new array
if a new medication treates the name amount, add it to the list
** ONLY ADD MEDICATIONS THAT TREAT AT LEAST ONE SYMPTOM
*/

function webMD(ailments, meds) {
    let output = [] // array that holds the names of the best medicines
    let treatedSymptomCount = 0 // how many ailments the best medicines can do
    for (let medication of meds) {
        // for each medicine, do the following:
        let curTreatedCount = 0
        for (let ailment of ailments) {
            // for each ailment given:
            if (medication.treatableSymptoms.includes(ailment)) {
                // the current medication can solve the symptom
                curTreatedCount++
            }
        }
        // at this point, we know how many ailments this medicine can treat
        if (curTreatedCount > treatedSymptomCount) { // if our current medicine can treat more ailments than our previous best
            output = [medication.name] // current medicine is the only best medicine, previous array is omitted
            treatedSymptomCount = curTreatedCount // update the number of ailments that the best medicine (the current one) can treat
        } else if (curTreatedCount == treatedSymptomCount && curTreatedCount > 0) { // if our current medicine can treat the same number of symptoms as the best; do not include medicines that treat 0 symptoms
            output.push(medication.name) // current medicine is one of the best medicines, add to the array
        }
        // leftover conditions: curTreatedCount is lower, or curTreatedCount is 0 -> do nothing
    }
    // at this point, only the best medicines are included in output
    return output
}

function webMD2(ailments, meds) {
    let treatedSymptomCount = 0
    const treatmentPlan = {}
    for (let i = 0; i < meds.length; i++) {
        const medication = meds[i]
        for (let treatSymptom of medication.treatableSymptoms) {
            if (treatmentPlan.hasOwnProperty(treatSymptom)) {
                treatmentPlan[treatSymptom].push(i)
            } else {
                treatmentPlan[treatSymptom] = [i]
            }
        }
    }
    // console.log(treatmentPlan.pain);
    // console.log(meds[1].name);
    const medEfficiency = {}
    for (let ailment of ailments) {
        if (!treatmentPlan.hasOwnProperty(ailment)) {
            continue
        }
        for (let medIdx of treatmentPlan[ailment]) {
            if (medEfficiency.hasOwnProperty(medIdx)) {
                medEfficiency[medIdx]++
            } else {
                medEfficiency[medIdx] = 1
            }
        }
    }
    let output = []
    let bestMedCount = 0
    for (let medIdx in medEfficiency) {
        if (medEfficiency[medIdx] > bestMedCount) {
            output = [meds[medIdx].name]
            bestMedCount = medEfficiency[medIdx]
        } else if (medEfficiency[medIdx] === bestMedCount) {
            output.push(meds[medIdx].name)
        }
    }
    return output
}

// console.log(webMD(["pain"], medications));
// console.log(webMD(["pain", "inflammation", "depression"], medications));
// console.log(webMD(["existential dread"], medications));
console.log(webMD2(["pain"], medications));
console.log(webMD2(["pain", "inflammation", "depression"], medications));
console.log(webMD2(["existential dread"], medications));