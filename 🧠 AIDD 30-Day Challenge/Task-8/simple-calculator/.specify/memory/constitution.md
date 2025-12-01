<!--
Sync Impact Report:
  Version change: 0.0.0 -> 1.0.0
  Modified principles:
    - [PRINCIPLE_1_NAME] -> I. Code Readability and Comments
    - [PRINCIPLE_2_NAME] -> II. Simple and Minimal UI
    - [PRINCIPLE_3_NAME] -> III. Reusable Logic
    - [PRINCIPLE_4_NAME] -> IV. Correct Calculator Output
    - [PRINCIPLE_5_NAME] -> V. Robust Error Handling
  Added sections:
    - Constraints
  Removed sections:
    - SECTION_3_NAME (Development Workflow, Review Process, Quality Gates)
    - SECTION_3_CONTENT
  Templates requiring updates:
    - .specify/templates/plan-template.md (Needs update in "Constitution Check" section)
    - .specify/templates/spec-template.md (Requirements should align with new principles)
    - .specify/templates/tasks-template.md (Task categorization to reflect new principle-driven task types)
  Follow-up TODOs: None.
-->
# Simple Calculator Constitution

## Core Principles

### I. Code Readability and Comments
Code MUST be readable, clean, and well-commented to ensure maintainability and understanding by all contributors.

### II. Simple and Minimal UI
The User Interface MUST be simple and minimal, exclusively using Streamlit to maintain consistency and ease of use.

### III. Reusable Logic
Logic MUST be implemented using reusable functions to promote modularity, reduce redundancy, and improve code organization.

### IV. Correct Calculator Output
The calculator MUST provide correct output for every operation, ensuring accuracy and reliability.

### V. Robust Error Handling
Error handling MUST be properly implemented to gracefully manage unexpected inputs and operational failures, enhancing user experience and system stability.

## Constraints

### I. Technology Stack
Only Python and Streamlit are permitted for development.

### II. Backend Separation
Backend logic MUST be separated from the UI to ensure clear architectural boundaries and facilitate future scalability.

### III. UI Library Restrictions
No external complex UI libraries are permitted beyond Streamlit.

### IV. Division by Zero
Division by zero errors are NOT allowed and MUST be handled appropriately.

## Governance
This constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance.

**Version**: 1.0.0 | **Ratified**: 2025-12-02 | **Last Amended**: 2025-12-02
