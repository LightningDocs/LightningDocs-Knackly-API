Dec 29, 2025
Update and rename Data Model Schema 1.3.8
Add new properties enableNonDutchAll (in "enableFeatures"); isNonDutchAll (in "loan"); isMaximumGuarantorLiability (in "guarantorInformation"); maximumLiabilityAmount (in "guarantors", "guarantorInformation"); legalDescriptionAbbreviated (in "collateral"); lastStepYearLength, extensionMargin, isDeferredFees, deferredFeeOrigination, deferredFeeBroker, deferredFeeDocumentPrep, deferredFeeAdministration, deferredFeePayoff,  deferredOriginationMonths, servicingFee, isHalfPayment, isCollateralReserve, and collateralReserve (in "features"); and memberNumber and mininumBalance (in "collateralSecurityAgreement")

Remove occupancyAgreementDeliveryDate property (in "documentCustomization"), add occupancyDeadlines array in its place.

Add "bank" to the list of enumerated values for collateralType (in "collateralSecurityAgreement").

Deprecate allocatedLoanAmount (in "collateralProperties", "collateral").

Update various titles and descriptions for clarity and accuracy.


Sep 21, 2025
Update and rename Data Model Schema 1.3.7
Switch former "description" values to the new "usage" key and change all "description" values to better describe the role the property in question plays within the transaction or loan documents.
Add descriptor "CONFIGURATION" to the "usage" of all properties that, rather than representing a fact about the transaction, simply configure the questionnaire or otherwise alter the user experience.
Add new client-specific properties throughout the data model.
Add new top-level properties "isNoScenario" and "scenarioName".These properties allow the integration to prevent the user from selecting a scenario within the application.
Add properties to the "enableFeatures" object and the "lenderInformation" object that allow the integration to send custom addresses (in place of the lender's notice address) for return of non-recordable documents and (separately) recordable documents.
Add properties to the "enableFeatures" object and the "documentCustomization" object that allow the integration to exclude the Lender's Closing Instructions from the assembled documents.
Add new property "releasePriceBuildingLoan" to the "collateralProperties" array properties, which allows the integration to specify a collateral release price for the New York Building Loan Agreement (in addition to using the "releasePrice" property to specify the same for the main loan).
Add properties to the "collateralProperties" array properties that allow the integration to give details on a tenancy in common agreement.
Rename "isEPA" property to "isEquityPledgeAgreement."


Jun 17, 2025
Update and Data Model Schema 1.3.6
Add "isForeignNational" property to the "grantors" definition.
Add the following top-level properties: "isCheckData", "customWorkItemName", "isBuildingLoanStandalone"
Add "isBuildingLoanIntended" property to the "features" object for use with the New York Building Loan feature.
Allow "assignmentOfPermitsProperties" to be sent both for "construction" and changed the version in "features" to "cannabisAssignmentOfPermitsProperties". When the same properties is entered for both the application automatically combines both assignments into one.
Add properties to allow attribution of a MERS number for loan assignee in the "loanSale" object.
Add various properties associated with client specific customizations.
Changed various titles and descriptions for clarity and consistency.


Mar 26, 2025
Update and rename 1.3.5
Add "professional limited liability company" as a valid option for all properties that use the "entityTypes" definition.
Borrowers, Non-Borrower Owners, Guarantors, and all their signers (down to the third level) can now have "owners" (and signers for their owners) defined for them.
Remove the following permissions from the "enableFeatures" object as these features now appear in the default interview for all users: "enableBorrowerServicingFees", "enableMERS", "enableTranslator", "enableW9".
The "trustee" property for "collateralProperties" objects now recommends that you leave this option unanswered unless the lender has a need for a specific trustee, as a generally satisfactory default is automatically applied within the produced documents.
Add properties for New York (C)EMA and Building Loan Agreements.
Add draws, inspection fee, and specified completion date options to the "construction" object.
Build additional capabilities and options into the automatic extension feature.
Add options for Guarantor W9s and Third Party Affiliates to the "additionalDocuments" object.
Add cash collateral feature to the "documentCustomization" object.
Add properties related to various client specific features.
Update numerous titles and descriptions to better correspond to the Lightning Docs interview.

Sep 24, 2024
Update and rename 1.3.4
Remove certain features to be allowed behind new permissions in the "enableFeatures" object, including: "enableInterestRateStep", "enableLineOfCredit", "enableMasterGuaranty", "enableProFormaPolicy", "enableDeferredPayments".

Add new feature to "features" object: "isDeferredPayments".

Add additional option for per diem interest delivery: "Delivery Instructions to be Provided".

All fee arrays in the "settlement" object now use "delivery" as the name of the property that describes how the fee is to be delivered. (Previously it was "comment" for some, "delivery" for others.)


Sep 3, 2024
Update and rename to 1.3.3
Add new property "transactionID". 

Add new permissions: "enableShtarIska", "enableWorkItemName", "enableFirstPaymentDate", "enableRemoveCognovit", and "enableBridgeToPerm". Split permission "enableNoFill" into two permissions: "enableNoFillCertNonOwner" and "enableNoFillBusinessPurpose". Changed permission "enableComplexSigners" to "enableEntityOwnership". 

In "titleInformation" object add "isRemoveTitleInsurance" property.

In "escrowInformation" object remove "address" property.

In "collateralProperties" array in "collateral" object add "allocatedLoanAmount" property.

In "features" object: Add "isPrepaymentPremium" property and remove "None" as an option for the "prepaymentPremium" property. Split "interestReserveAmount" into two properties (to be used depending on the answer to "interestReserve"): "interestReserveDollars" ("Dollar Amount") and "interestReserveMonths" ("Monthly Payments"). Add "appraisalARV" property. Split "defaultReserveAmount" into two properties (to be used depending on the answer to "defaultReserve"): "defaultReserveDollars" ("Amount") and "defaultReserveMonths" ("Months"). Add "isShtarIska" property. In "construction" object add the following: "draws" property, "isConstructionCompletionGuaranty" property, and "constructionCompletionGuarantors" array.

Complete schemas for "collateralSecurityAgreement" and "equityPledgeAgreement".

Make significant changes to titles and discriptions throughout the data model to better align them with the interview and to add clarity (will not alter functionality).

Change numerous properties of "number" type to "integer" type to make it more clear which properties accept decimal values.
