# Data Model Schema Changelog

## Version 1.3.12 — October 12, 2026

### New Properties

#### Top-Level

- `lendersAttorney` (new object)

#### `lendersAttorney`

- `name`
- `email`
- `firm`

#### `collateral`

- `isLotSplit`
- `isSpecifyReleaseprice`
- `releasePricingType`

#### `collateral.collateralProperties`

- `numberOfLots`

#### `loan`

- `isAmortizationSchedule`
- `isChangeLastPayment`
- `dartULINumber`
- `isMaturityDateBasedOnDocDate`

#### `features`

- `permanentPhaseInterestRate`

#### `features.impounds`

- `aggregateAdjustmentAmount`

#### `additionalDocuments`

- `assignments` (new array)
- `isSingleMemberAffidavit`
- `singleMemberAffidavitEntityName`

#### `additionalDocuments.assignments`

- `assignee`
- `assignmentDate`
- `assigneeName`
- `recordingAttention`
- `assigneeAddress`
- `isAltRecordingAddress`
- `altRecordingName`
- `altRecordingAttention`
- `altRecordingAddress`
- `isMERSAssignee`
- `mersNumber`

#### `documentCustomization`

- `customNotaryAcknowledgmentBaseState`
- `customNotaryAcknowledgmentSignerStates` (new object)
- `additionalProvisions` (new array)

#### `documentCustomization.customNotaryAcknowledgmentSignerStates`

- `individualName`
- `signingState`

#### `documentCustomization.additionalProvisions`

- `category`
- `header`
- `provision`

### Deprecated Properties

#### `collateral`

- `partialRelease`
- `isScheduleOfReleasePrices`
- `customNotaryAcknowledgmentState`

#### `additionalDocuments`

- `assignee`
- `assigneeInformation`
- `assignmentDate`
- `isAssignmentResale`
- `isAssigneeUsingMers`
- `assigneeMersNumber`

### Removed Properties

#### `collateral`

- `usesScheduleOfProperties`
- `allocatedLoanAmount` (previously deprecated)

### Other Changes

- Updated various descriptions, titles, and usage notes for accuracy.

---

## Version 1.3.10 — June 15, 2026

### New Permissions

Added the following permissions to `enableFeatures`:

- `enableAdditionalCovenants`
- `enableDARTLanguage`
- `enableAmortizationSchedule`
- `enableServicerAccountNumber`
- `enableAdditionalImpoundsCityCountyEtc`

### New Properties

#### Grantors (definition)

- `beneficialOwners`

#### Top-Level

- `bankName_ACH`
- `bankDraftingPaymentsDay`
- `servicerAccountNumber`

#### `borrowerInformation`

- `noticeEmail`
- `noticePhone`

#### `brokerInformation`

- `yieldSpreadPremium`

#### `preparerInformation`

- `phone`

#### `closingContact`

- `phone`

#### `collateral`

- `isScheduleOfReleasePrices`
- `releasePriceSchedule`
- `releasePriceMultiplier`

#### `collateral.collateralProperties`

- `manualVesting`

#### `collateral.collateralProperties.seniorLiens`

- `lenderAddress`
- `accountNumber`

#### `loan`

- `isInterestRateReduction`
- `interestRateReduction`
- `isDARTLanguage`

#### `features`

- `deferredFeeDocumentDraw`
- `deferredFeeReconveyance`
- `deferredFeeSubordination`
- `deferredFeeUCC`
- `cashLiquidityAmount`
- `isCashCollateralAccount`
- `cashCollateralMinimumBalance`
- `cashCollateralDisbursementConditions`

#### `features.construction`

- `isSequentialDrawLanguage`
- `isAssignmentOfPermitsAll`

#### `features.impounds`

Initial tax fields:

- `initialCityTax`
- `initialCountyTax`
- `initialSchoolTax`
- `initialTownTax`
- `initialVillageTax`

Monthly tax fields:

- `monthlyCityTax`
- `monthlyCountyTax`
- `monthlySchoolTax`
- `monthlyTownTax`
- `monthlyVillageTax`

#### `settlement`

- `perDiemDays`

#### `additionalDocuments`

- `is4506C`

#### `additionalDocuments.propertyManagement`

- `isAllProperties`
- `propertiesSelect`

#### `documentCustomization`

- `reportingFrequency`
- `isCompensatingBalance`
- `compensatingBalancePercent`
- `isAdditionalCovenants`
- `additionalCovenants`

#### `equityPledgeAgreement`

- `isContractForDeed`

### Other Changes

- Updated various descriptions, titles, and usage notes for accuracy.

---

## Version 1.3.8 — December 29, 2025

### New Properties

#### `enableFeatures`

- `enableNonDutchAll`

#### `loan`

- `isNonDutchAll`

#### `guarantorInformation`

- `isMaximumGuarantorLiability`

#### `guarantors`
#### `guarantorInformation`

- `maximumLiabilityAmount`

#### `collateral`

- `legalDescriptionAbbreviated`

#### `features`

- `lastStepYearLength`
- `extensionMargin`
- `isDeferredFees`
- `deferredFeeOrigination`
- `deferredFeeBroker`
- `deferredFeeDocumentPrep`
- `deferredFeeAdministration`
- `deferredFeePayoff`
- `deferredOriginationMonths`
- `servicingFee`
- `isHalfPayment`
- `isCollateralReserve`
- `collateralReserve`

#### `collateralSecurityAgreement`

- `memberNumber`
- `minimumBalance`

### Replaced Properties

Removed:

- `occupancyAgreementDeliveryDate`

Added:

- `occupancyDeadlines` (array)

### Other Changes

- Added `"bank"` as a valid `collateralType` value in `collateralSecurityAgreement`.
- Deprecated `allocatedLoanAmount` in `collateralProperties` and `collateral`.
- Updated various titles and descriptions for clarity and accuracy.

---

## Version 1.3.7 — September 21, 2025

### Documentation Improvements

- Migrated former `description` values to the new `usage` key.
- Updated all `description` values to better describe each property's role in the transaction and generated documents.
- Added the `CONFIGURATION` usage descriptor to properties that affect interview behavior rather than transaction data.

### New Properties

#### Top-Level

- `isNoScenario`
- `scenarioName`

These properties allow integrations to prevent users from selecting a scenario within the application.

### Additional Enhancements

- Added client-specific properties throughout the data model.
- Added support for custom addresses for returning recordable and non-recordable documents.
- Added support for excluding Lender's Closing Instructions from assembled documents.
- Added `releasePriceBuildingLoan` to `collateralProperties`.
- Added tenancy-in-common related properties to `collateralProperties`.

### Renamed Properties

| Previous Name | New Name |
|--------------|-----------|
| `isEPA` | `isEquityPledgeAgreement` |

---

## Version 1.3.6 — June 17, 2025

### New Properties

#### `grantors`

- `isForeignNational`

#### Top-Level

- `isCheckData`
- `customWorkItemName`
- `isBuildingLoanStandalone`

#### `features`

- `isBuildingLoanIntended`

### Feature Enhancements

- `assignmentOfPermitsProperties` can now be provided for both construction and cannabis permit assignments.
- Added MERS number support for loan assignees in `loanSale`.
- Added multiple client-specific customization properties.

### Other Changes

- Updated titles and descriptions for clarity and consistency.

---

## Version 1.3.5 — March 26, 2025

### New Capabilities

- Added `"professional limited liability company"` as a valid value wherever the `entityTypes` definition is used.
- Borrowers, Non-Borrower Owners, Guarantors, and their signers can now have nested ownership structures and signer hierarchies.

### Removed Permissions

The following permissions were removed from `enableFeatures` because the associated features are now available by default:

- `enableBorrowerServicingFees`
- `enableMERS`
- `enableTranslator`
- `enableW9`

### New Features

- Added support for New York (C)EMA and Building Loan Agreements.
- Added construction draw schedules, inspection fees, and specified completion dates.
- Expanded automatic extension functionality.
- Added Guarantor W-9 and Third Party Affiliate options.
- Added cash collateral options to `documentCustomization`.
- Added various client-specific feature properties.

### Documentation Updates

- Updated numerous titles and descriptions to better align with the Lightning Docs interview.

---

## Version 1.3.4 — September 24, 2024

### Permission Changes

The following features were moved behind new permissions in `enableFeatures`:

- `enableInterestRateStep`
- `enableLineOfCredit`
- `enableMasterGuaranty`
- `enableProFormaPolicy`
- `enableDeferredPayments`

### New Features

#### `features`

- `isDeferredPayments`

### Other Changes

- Added `"Delivery Instructions to be Provided"` as a per diem interest delivery option.
- Standardized all fee arrays in `settlement` to use the property name `delivery` for delivery instructions.

---

## Version 1.3.3 — September 3, 2024

### New Properties

#### Top-Level

- `transactionID`

### New Permissions

- `enableShtarIska`
- `enableWorkItemName`
- `enableFirstPaymentDate`
- `enableRemoveCognovit`
- `enableBridgeToPerm`

### Permission Changes

- Split `enableNoFill` into:
  - `enableNoFillCertNonOwner`
  - `enableNoFillBusinessPurpose`

- Renamed:
  - `enableComplexSigners` → `enableEntityOwnership`

### Additional Changes

#### `titleInformation`

- Added `isRemoveTitleInsurance`

#### `escrowInformation`

- Removed `address`

#### `collateral.collateralProperties`

- Added `allocatedLoanAmount`

#### `features`

Added:

- `isPrepaymentPremium`
- `appraisalARV`
- `isShtarIska`

Split:

- `interestReserveAmount` into:
  - `interestReserveDollars`
  - `interestReserveMonths`

- `defaultReserveAmount` into:
  - `defaultReserveDollars`
  - `defaultReserveMonths`

#### `features.construction`

Added:

- `draws`
- `isConstructionCompletionGuaranty`
- `constructionCompletionGuarantors`

### Major Enhancements

- Completed schemas for:
  - `collateralSecurityAgreement`
  - `equityPledgeAgreement`

### Documentation Updates

- Significantly revised titles and descriptions throughout the model to improve alignment with the interview experience and increase clarity.
- Converted numerous `number` properties to `integer` where decimal values are not accepted.