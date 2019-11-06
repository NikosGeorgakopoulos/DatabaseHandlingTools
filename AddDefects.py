developers = {
    "Developers": [
        {
            "Developer": {
                "Name": "John Doe",
                "Business Areas": [
                    "Liabilities",
                    "Trade Finance",
                    "Retail Assets",
                    "General Banking",
                    "Corporate Assets",
                    "GL&Accounting"  
                ],
                "Experience": "3",
                "Types of Expertise": [
                    "Software Error",
                    "UI Error"
                ],
                "General Skillset": [
                    "Database",
                    "SQL",                    
                    "IIS",                    
                    "Web Recording",
                    "Web Execution",
                    "XPath",
                    "General Enquiries"

                ]
            }
        },
        {
            "Developer": {
                "Name": "Jane Goodall",
                "Business Areas": [
                    "Technical",
                    "SIB Report Issue",
                    "SMS User Profile",
                    "T24 Report Issue",
                    "Interfaces",
                    "Investment Banking"


                ],
                "Experience": "2",
                "Types of Expertise": [
                    "Software Error",
                    "Configuration Error"
                ],
                "General Skillset": [
                    "CSV",
                    "SQL",
                    "IIS",
                    "XPath",
                    "Installation",
                    "SMS"
                ]
            }
        },
        {
            "Developer": {
                "Name": "Enrico Fermi",
                "Business Areas": [
                    "Technical",
                    "SIB Report Issue",
                    "SMS User Profile",
                    "T24 Report Issue",
                    "Interfaces",
                    "Investment Banking"
                ],
                "Experience": "3",
                "Types of Expertise": [
                    "Software Error"
                ],
                "General Skillset": [
                    "Database",
                    "SQL",
                    "CASH POOL"
                ]
            }
        },
        {
            "Developer": {
                "Name": "Max Planck",
                "Business Areas": [
                    "COB Error",
                    "HPS / AFS",
                    "Retail & Corporate Assets Contracts",
                    "Critical",
                    "Profit Distribution",
                    "Internet & Mobile Banking",
                    "Cash Pool FSD"

                ],
                "Experience": "4",
                "Types of Expertise": [
                    "Software Error",
                    "UI Error",
                    "Configuration Error"                    
                ],
                "General Skillset": [
                    "Database",
                    "SQL"
                ]
            }
        },
        {
            "Developer": {
                "Name": "Josh Barry",
                "Business Areas": [
                    "Liabilities",
                    "Trade Finance",
                    "Retail Assets",
                    "General Banking",
                    "Corporate Assets",
                    "GL&Accounting"             

                ],
                "Experience": "5",
                "Types of Expertise": [
                   "Configuration Error"
                ],
                "General Skillset": [
                    "Database",
                    "SQL",
                    "IIS",
                    "Report"
                ]
            }
        }
    ],
    "Experience Levels": [
        {
            "ID": "1",
            "Value": "Trainee"
        },
        {
            "ID": "2",
            "Value": "Novice"
        },
        {
            "ID": "3",
            "Value": "Junior"
        },
        {
            "ID": "4",
            "Value": "Intermediate"
        },
        {
            "ID": "5",
            "Value": "Senior"
        }
    ]
}


import requests
requests.post('http://localhost:5100/addDeveloper/hashId/63014800A811AB4CB366DC008E67FE65', json=developers)
