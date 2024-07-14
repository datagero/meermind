export interface StudentSummary {
    "summaryTitle": string,
    "summaryPoints": string[]
}

export interface Note {
    "title": string,
    "oneLineSummary": string,
    "studentSummary": StudentSummary[],
    "relatedInformation": string[],
    "benefits": string[],
    "limitations": string[],
    "realWorldExample": string,
    "stateOfTheArtResearch":string,
    "references": string[]
}