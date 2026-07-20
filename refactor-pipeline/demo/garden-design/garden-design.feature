# Generated from Xray export ADIOSMAU 2026-05-04.
# Pair with garden-design.spec.md (entities, state machine, dependencies)
# and garden-design.coverage.md (gaps & open questions).
#
# Tag conventions:
#   @ADIOSMAU-xxx     traceability to the source Xray test
#   @validation       step gating / enable-disable rules
#   @generation       image generation pipeline
#   @persistence      cross-flow state retention
#   @paywall          premium gating
#   @analytics        amplitude events
#   @firebase         remote-config-driven behavior
#   @offline          network failure paths
#   @i18n             localisation
#   @manual-only      not unit-testable (visual/quality assertions) — exclude from codegen
#   @internal         debug/QA-only paths

@feature:garden_design
Feature: Garden Design

  As a user, I generate AI-rendered garden images from a photo by choosing a
  style and a color palette across three sequential steps. See
  garden-design.spec.md for entities, state machine, and external dependencies.

  Background:
    Given the user is on the main screen
    And the user enters the Garden Design flow


  # ──────────────────────────────────────────────────────────────────
  # Step 1 — photo input
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-144 @validation
  Scenario: Continue is disabled on step 1 when no photo is provided
    Given the user is on step 1 with no photo selected
    Then the Continue control is disabled

  @ADIOSMAU-167 @camera
  Scenario Outline: A captured photo appears in the step 1 placeholder
    Given the user is on step 1
    When the user captures a photo via the camera in <orientation> orientation
    Then the captured photo is shown in the step 1 placeholder

    Examples:
      | orientation |
      | portrait    |
      | landscape   |

  @ADIOSMAU-145 @edge-case
  Scenario: Selecting a template after capturing a photo requires confirmation
    Given the user has captured a photo on step 1
    When the user selects an example template
    Then a replace-photo confirmation prompt is shown
    And the captured photo is unchanged until the user confirms

  @ADIOSMAU-145 @edge-case
  Scenario: Dismissing the replace-photo prompt keeps the original photo
    Given the user has captured a photo on step 1
    And the user has triggered the replace-photo confirmation by selecting a template
    When the user dismisses the confirmation
    Then the captured photo remains in the step 1 placeholder

  @ADIOSMAU-145 @edge-case
  Scenario: Confirming the replace-photo prompt swaps the photo for the template
    Given the user has captured a photo on step 1
    And the user has triggered the replace-photo confirmation by selecting a template
    When the user confirms the replacement
    Then the template is shown in the step 1 placeholder

  @ADIOSMAU-175 @validation
  Scenario: Multi-tap on Continue advances exactly one step
    Given the user has provided a photo on step 1
    When the user taps Continue 3 times in rapid succession
    Then the flow is on step 2

  @ADIOSMAU-175 @analytics
  Scenario: Multi-tap on Continue does not duplicate analytics events
    Given the user has provided a photo on step 1
    When the user taps Continue 3 times in rapid succession
    Then the analytics event for advancing to step 2 is emitted exactly once


  # ──────────────────────────────────────────────────────────────────
  # Step 2 — style selection
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-213 @validation
  Scenario: Continue is disabled on step 2 when no style is selected
    Given the user is on step 2 with no style selected
    Then the Continue control is disabled

  @ADIOSMAU-307 @persistence
  Scenario: Last saved custom prompt is preselected on a subsequent flow
    Given the user has previously completed step 2 with a custom prompt "modern Japanese zen"
    When the user starts a new Garden Design flow and reaches step 2
    Then the custom-prompt option is selected with text "modern Japanese zen"


  # ──────────────────────────────────────────────────────────────────
  # Step 3 — palette selection
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-159 @validation
  Scenario: Generate is disabled on step 3 when no palette is selected
    Given the user is on step 3 with no palette selected
    Then the Generate control is disabled

  @ADIOSMAU-306 @palette
  Scenario: Surprise-me selects a random enabled palette
    Given the user is on step 3
    And the available enabled palettes are ["earthy", "vibrant", "monochrome", "pastel"]
    When the user selects the surprise-me option
    Then exactly one palette from the available enabled palettes is applied
    And the chosen palette is selected uniformly at random across repeated invocations

  @ADIOSMAU-305 @firebase @entitlement
  Scenario Outline: Palettes on step 3 reflect Firebase entitlement state
    Given Firebase has a palette "<palette>" with entitlement "<entitlement>"
    When the user reaches step 3
    Then the palette "<palette>" <visibility>
    And the premium-icon badge is <badge>

    Examples:
      | palette | entitlement | visibility   | badge      |
      | p_free  | free        | is visible   | not shown  |
      | p_prem  | premium     | is visible   | shown      |
      | p_block | blocked     | is not shown | not shown  |

  @ADIOSMAU-93 @firebase @internal
  Scenario: Original style tile visibility follows Firestore flag
    Given the Firestore flag styles/styleOriginalStyle is disabled
    When the user reaches step 2
    Then the Original style tile is not present
    When the Firestore flag styles/styleOriginalStyle is enabled
    And the user reaches step 2
    Then the Original style tile is present

  @ADIOSMAU-93 @firebase @internal
  Scenario: Original palette tile visibility follows Firestore flag
    Given the Firestore flag gardenDesignColorPalettes/colorPaletteOriginalPalette-0 is disabled
    When the user reaches step 3
    Then the Original palette tile is not present
    When the Firestore flag gardenDesignColorPalettes/colorPaletteOriginalPalette-0 is enabled
    And the user reaches step 3
    Then the Original palette tile is present


  # ──────────────────────────────────────────────────────────────────
  # Generation
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-158 @generation
  Scenario: Tapping Generate with all inputs set issues a generation request
    Given the user has provided a photo, a style, and a palette
    When the user taps Generate on step 3
    Then a generation request is issued with the chosen photo, style, and palette
    And the result image is returned within 45 seconds

  @ADIOSMAU-158 @manual-only
  Scenario: Generated image is of acceptable visual quality
    Given a successful generation request
    Then the result image is of acceptable quality
    And the result image reflects the parameters chosen on steps 1, 2, and 3

  @ADIOSMAU-94 @generation
  Scenario Outline: Original style + Original palette generates from <source>
    Given the user has provided a photo via <source>
    And the user has selected the Original style on step 2
    And the user has selected the Original palette on step 3
    When the user taps Generate
    Then a generation request is issued and succeeds

    Examples:
      | source  |
      | camera  |
      | gallery |

  @ADIOSMAU-315 @generation @template
  Scenario: Original style + Original palette generates from a template
    Given the user has selected an existing template on step 1
    And the user has selected the Original style on step 2
    And the user has selected the Original palette on step 3
    When the user taps Generate
    Then a generation request is issued and succeeds

  @ADIOSMAU-146 @persistence
  Scenario Outline: Successful generation result is persisted to Projects (<source>)
    Given the user has provided a photo via <source>
    And the user has selected a style and a palette
    When the user taps Generate and the request succeeds
    Then the result is appended to the user's Projects listing

    Examples:
      | source  |
      | camera  |
      | gallery |


  # ──────────────────────────────────────────────────────────────────
  # Cancellation & connectivity
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-308 @cancel
  Scenario: Cancelling on step 3 returns to main and discards in-flow state
    Given the user has completed step 1 with a photo
    And the user has completed step 2 with a style
    And the user is on step 3
    When the user dismisses the flow via the header close control
    Then the user is on the main screen
    And the in-flow photo, style, and palette selections are not retained

  @ADIOSMAU-313 @offline
  Scenario: Offline at generate-time presents the No Internet screen
    Given the user has provided a photo, a style, and a palette
    And the device has no network connectivity
    When the user taps Generate
    Then the No Internet screen is presented

  @ADIOSMAU-313 @offline
  Scenario: Try-again while still offline keeps the No Internet screen
    Given the No Internet screen is presented after a failed generate attempt
    And the device has no network connectivity
    When the user taps Try again
    Then the No Internet screen remains presented

  @ADIOSMAU-313 @offline
  Scenario: Try-again after connectivity returns proceeds with generation
    Given the No Internet screen is presented after a failed generate attempt
    And the device has network connectivity
    When the user taps Try again
    Then a generation request is issued and succeeds


  # ──────────────────────────────────────────────────────────────────
  # Monetisation
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-212 @paywall
  Scenario: Selecting a PRO template presents the Payment screen
    Given the Garden Design entry shows a footer with templates
    When the user selects a template with tier "pro"
    Then the Payment screen is presented


  # ──────────────────────────────────────────────────────────────────
  # Localisation
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-310 @i18n
  Scenario Outline: Step copy renders for locale <locale>
    Given the device locale is <locale>
    When the user navigates through steps 1, 2, and 3
    Then all step copy resolves to a non-empty localised string for <locale>
    And no copy falls back to the localisation-key identifier

    Examples:
      # confirm against Localizable.strings — list below is a placeholder
      | locale |
      | en     |
      | es     |
      | fr     |
      | de     |
      | pt     |


  # ──────────────────────────────────────────────────────────────────
  # Analytics
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-1284 @analytics
  Scenario: Entering Garden Design fires start_garden once with no properties
    When the user enters the Garden Design flow
    Then the analytics event "start_garden" is emitted exactly once
    And the event has no properties

  @ADIOSMAU-1284 @analytics
  Scenario Outline: Each step view fires view_screen_garden with the step number
    When the user views step <screen_number>
    Then the analytics event "view_screen_garden" is emitted with property screen_number = <screen_number>

    Examples:
      | screen_number |
      | 1             |
      | 2             |
      | 3             |


  # ──────────────────────────────────────────────────────────────────
  # First-run / UI (visual — manual only)
  # ──────────────────────────────────────────────────────────────────

  @ADIOSMAU-314 @first-run
  Scenario: First-time tooltip is shown on first entry to Garden Design
    Given the user is opening Garden Design for the first time on this install
    When the Garden Design entry renders
    Then the tooltip overlay is presented

  @ADIOSMAU-314 @first-run
  Scenario: Tooltip can be dismissed and is not shown again
    Given the tooltip overlay is presented
    When the user dismisses the tooltip
    And the user re-enters Garden Design
    Then the tooltip overlay is not presented

  @ADIOSMAU-157 @manual-only
  Scenario Outline: Garden Design renders correctly in <appearance> mode
    Given the device appearance is <appearance>
    When the user views the Garden Design entry
    Then the layout matches the Figma masterfile

    Examples:
      | appearance |
      | light      |
      | dark       |
