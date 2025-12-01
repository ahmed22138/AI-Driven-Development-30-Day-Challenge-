# Tasks: Simple Calculator

**Input**: Design documents from `/specs/1-simple-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Included as recommended by the plan for good practice.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `calculator/`, `tests/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project folder `calculator/` at project root
- [ ] T002 Initialize Python project and install Streamlit (`pip install streamlit`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T003 Set up basic test directory structure `tests/unit/` and `tests/integration/` at project root

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Implement the core calculator functionality with UI and error handling for basic arithmetic operations.

**Independent Test**: The Streamlit application can be launched, and all arithmetic operations (add, subtract, multiply, divide, including division by zero error handling) can be tested directly via the UI, displaying correct results.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T004 [P] [US1] Write unit tests for `add`, `subtract`, `multiply`, `divide` functions in `tests/unit/test_calculator.py`
- [ ] T005 [US1] Write an integration test for the Streamlit UI flow, covering number input, operation selection, calculate button click, and result display, including division by zero in `tests/integration/test_app.py`

### Implementation for User Story 1

- [ ] T006 [P] [US1] Create `calculator.py` in `calculator/` directory
- [ ] T007 [P] [US1] Implement `add(a, b)` function in `calculator/calculator.py`
- [ ] T008 [P] [US1] Implement `subtract(a, b)` function in `calculator/calculator.py`
- [ ] T009 [P] [US1] Implement `multiply(a, b)` function in `calculator/calculator.py`
- [ ] T010 [P] [US1] Implement `divide(a, b)` function with division by zero handling in `calculator/calculator.py`
- [ ] T011 [US1] Create `app.py` in `calculator/` directory
- [ ] T012 [US1] Set up Streamlit UI in `calculator/app.py` with input fields for two numbers
- [ ] T013 [US1] Add a dropdown or radio buttons for operation selection in `calculator/app.py`
- [ ] T014 [US1] Add a "Calculate" button in `calculator/app.py`
- [ ] T015 [US1] Connect UI inputs and button to call backend arithmetic functions from `calculator/calculator.py` in `calculator/app.py`
- [ ] T016 [US1] Display the calculation result and any error messages (e.g., division by zero) in `calculator/app.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T017 Code cleanup and refactoring in `calculator/` files
- [ ] T018 Final review and validation against `quickstart.md`
- [ ] T019 (Optional) Prepare for final deployment (e.g., `requirements.txt` generation, deployment script)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Arithmetic functions (`calculator.py`) before UI integration (`app.py`)

### Parallel Opportunities

- Tasks marked [P] can run in parallel (different files, no dependencies)
- All unit test writing tasks (T004) can be done in parallel.
- All individual arithmetic function implementations (T007-T010) can be done in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
