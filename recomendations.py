#!/usr/bin/python
# -*- coding: utf-8 -*-

#sha256 converter 
#https://passwordsgenerator.net/sha256-hash-generator/
recomendations = [
    ["File Create",
    "Is Scope Details Involves New File Or Files Or Folder? Or It Will Created Run Time?",
    "It Is Recomended, That File Do Not Have Vulnarability And Directly Accessible Without Login. \nhttps://www.youtube.com/watch?v=dRYy6gJBmyM",
    "File",
    "500",
    "Manual"
    ],
    ["Thirdparty Code",
    "Is There Any Library Or Code Used Which Is Provided By Someone Else Or Directly Downloaded From The Internet?",
    "It Is Recommended, To Go With A Manual Review.",
    "3rd Party",
    "500",
    "Auto,Manual"
    ], 
    ["Directory Traversal",
    "Any File Name Or File Parameters Are Passed Through Any Request Parameters Like Get/Post/Request ? Or File Path Is Stored In Local Storage Or Cookie For Further Use?",
    "It Is Recomended, To Add Proper Validation And Restrictions As Per Secure Coding Guide.",
    "File",
    "500",
    "Manual"
    ]
    , 
    ["File Access",
    "File Read | Upload | Download Functionality Involves?",
    "It Is Recomended, To Add Proper Validation And Restrictions As Per Secure Coding Guide. \nFor More https://www.youtube.com/watch?v=dRYy6gJBmyM",
    "File",
    "1000",
    "Manual"
    ],
    ["Payment Card Details",
    "credit/debit card details or any other payment card related card informaions are being used/processed/accessed?",
    "It Is Recomended, To Add Proper Restrictions As Per Secure Coding Guide.\nFor More https://www.youtube.com/watch?v=tAMx_fVKgTA",
    "PCI",
    "1000",
    "Manual"
    ],
    ["General Information",
    "Is GDPR related Informations are being accessed/display without authentication or being being log?",
    "It Is Recommended, To Apply authentication.\nFor More https://www.youtube.com/watch?v=j6wwBqfSk-o",
    "GDPR",
    "300",
    "Manual"
    ],
    ["InputValidation",
    "$_Get/$_Post/$_Request Is Used In Your Code Without Proper Validation?",
    "It Is Recomended, To Add Proper Validation And Restrictions As Per Secure Coding Guide.",
    "Validations",
    "300",
    "Manual"
    ],
    ["Unautorizedaccess",
    "File/Module/Api Directly Accessible From The Web Browser Without Any Authentication Or Access Control?",
    "It Is Recomended, To Implment access controll.\nFor More https://www.youtube.com/watch?v=0xEuncIHgv0",
    "Validations",
    "300",
    "Manual"
    ],
    ["Log",
    "Credit Card Related Details, Session Id, Server Connection Details Are Being Logged?",
    "It Is Recomended, Not To Log Any Sensitive Details, In Case Of Need You Can Use Proper Encryption.",
    "Validations",
    "300",
    "No"
    ],
    ["API Call",
    "Any Api Is Created Which Exchange Data From The Production Environment",
    "It Is Recommended, To Add Access & Authentication Control, Implement Throttling & Control.\nFor More https://drive.google.com/file/d/1oIWVZ5qUIhWMQ6qqVlPWELO_Wo4QHjnO/view?usp=sharing",
    "Validations",
    "300",
    "No"
    ]    
]
