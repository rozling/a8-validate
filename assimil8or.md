ASSIMIL8OR
Multi-Timbral Phase
Modulation Sampler

Operation Manual
040618

Copyright 2018 Rossum Electro-Music LLC
<www.rossum-electro.com>

Contents

1. Introduction
2. Module Installation
3. Assimil8or Overview
4. Basic Functionality
5. The Main Display
6. Managing SD Cards, Folders, Presets, and Samples
7. Sampling
8. Sample Start and End
9. Channels
10. Zones
11. Play Mode/Latch
12. Envelope
13. Loop Mode
14. Loop Start and End/Length
15. Pitch
16. Level
17. Phase Modulation
18. Mutate
19. Shuttle and Scrub
20. Pan/Mix
21. Utilities
22. Sample Sounds and Demos
23. Calibration
24. Specifications
25. From Dave’s Lab: Intro to Phase Modulation
26. From Dave’s Lab: Circuit Protection
27. Acknowledgements

# 1. Introduction

Thanks for purchasing (or otherwise
acquiring) the Assimil8or Multi-Timbral Phase
Modulation Sampler.

This manual will give you the information you need to get the most out of Assimil8or. The manual  assumes you already have a basic understanding of synthesis, synthesizers and samplers. If you’re just starting out, there are a number of good reference and tutorial resources available to get you up to speed.  One that we highly recommend is:

Power Tools for Synthesizer Programming
(2nd Edition)
By Jim Aikin
Published by Hal Leonard
HL00131064

## Support

In the unlikely event that you have a problem
with your Assimil8or, tell us about it here:

<http://www.rossum-electro.com/support/>
support-request-form/

…and we’ll get you sorted out.

If you have any questions, comments, or just want to say “Hi!,” you can always get in touch here:

<http://www.rossum-electro.com/about-2/>
contact-us/

…and we’ll get back to you.

Happy music making!

## Be Sure You Have the Latest Firmware

If we’ve released an updated version of firmware after your module was shipped to your dealer, you should update to that latest version(s) before proceeding.

To check:
  > Press the UTILITY button to bring up the Utilities screen. Scroll down to About this Module and click the encoder to see the currently installed version.

  > On the web, go to the Downloads tab at <www.rossum-electro.com/> products/ assimil8or/ and note the latest firmware version.

  > If it’s the same as the version in your module, you’re good to go. If not, follow the instructions there to update your module.

# 2. Installation

As you will have no doubt noticed, the rear of Assimil8or is a circuit board with a daughter board, exposed parts, and connectors. When handling Assimil8or, it’s important that the back of the module never come in contact with any metal (e.g. rails, patch cords, etc.) while under power. Consequently, power never be applied unless the module is screwed in to the rack, and no loose patch cords can find their way behind the panel through adjacent empty spaces.

Additionally, there is alway a small risk of damage by static electricity. Particularly on dry, cold days (or if you’ve just shuffled across your shag carpet in fuzzy slippers), make a point of touching the metal panel first, before touching any other part of the module.

While all Rossum Electro-Music modules are protected against reverse polarity damage, both to your module and your system, care should still be taken to connect the power cable correctly. (For more detail on our unique protection method, check out Dave’s discussion of Circuit Protection in Chapter 26.)

Plug the included 16-pin connector into the header on the rear of the module such that the red stripe on the cable (the -12V side) is on the same end of the header as the “Red Stripe (-12V)” text on the PCB.

Assimil8or requires, 220mA of +12V and 30mA of -12V, so be sure your power supply has sufficient capacity to handle it.

We have included both M3 and M2.5 (for vector rails) mounting screws. Use what fits your system.

If rack rash is of concern to you, use the included nylon washers when mounting Assimil8or in your case.

# 3. Overview

## What is Assimil8or?

Designed to provide a powerful, flexible sampling engine for modular synthesis, the Assimil8or Multi-Timbral Phase Modulation Sampler module is the latest incarnation of Dave Rossum’s decades-long pioneering of affordable professional sampling technology.

Assimil8or provides eight independent channels of sampled sounds (or control voltages), transposable over an astonishing range of up to +6 octaves (at 48kHz sample rate) and virtually limitlessly downward, with sound quality that can range from extremely hi-fi to low-fi, all with extensive real-time CV variable attack and release times.

  > 24 CV inputs that can be arbitrarily assigned to any parameters on any channels.

Examples include:
Pitch
Level
Bit Depth
Aliasing
Phase Modulation
Mix Pan
Sample Start
Sample Length
Loop Start
Loop End/Length
Envelope Attack and Release
Channel Zone
Crossfade Group Crossfade
And more…

  > A front panel accessible SD card for sample and preset storage.

In the following sections, we’ll look at each of Assimil8or’s functions in turn.
control.

Key Assimil8or features include:

  > Eight-channel multi-timbral operation.  Each channel is available from its own independent output as well as (optionally) appearing in the stereo mix output.
  > 422MB of sample memory, freely allocatable between the 8 channels.
  > Eight sample zones per channel, for CV- controlled sample selection.
  > Superb 24-bit A/D and D/A conversion.
  > Mono or stereo sampling. Channels can be configured as eight mono voices, four stereo voices, or any combination. (Well, any combination that adds up to eight).
  > Link Mode to create multilayered sounds under the control of a single trigger
  > Cycle Mode to allow one trigger source to sequentially trigger multiple channels, allowing repeatedly triggered sounds (e.g., a ride cymbal) to overlap (among other effects).
  > Crossfade Groups to crossfade between 2 to 8 channels under CV control.
  > Unique timbral capabilities with the ability to phase modulate samples by external analog signals or by other samples (a first, we believe).
  > 24 CV inputs that can be arbitrarily assigned to any parameters on any channels.
  > Variable sample fidelity with independently controllable anti-aliasing and bit depth under CV control.
  > Extensive sample manipulation and looping capabilities.
  > One-shot or gated sample playback with

# 4. Basic Functionality

Before we jump into individual functions, let’s take a look at Assimil8or’s basic organization.

## Power Up

When Assimil8or powers up, it remembers the most recently loaded folder and preset.  If the appropriate card is present, it will automatically load that folder and preset.

## Inputs

### Sample Inputs

Here’s where you input the signals to be sampled by Assimil8or. The inputs can be treated as stereo inputs or independent mono inputs. Sampling is configured in the Sampling Setup module described in Chapter 7.

A signal at a sample input can also be selected as a phase modulation source in the Phase Modulation module.

The Inputs accept a signal level up to +/- 10V full scale.

NOTE: Assimil8or is DC coupled throughout, so CVs as well as audio can be sampled (although you can choose to AC couple sampling in the Sample Setup screen if you so desire).

### Gate/Trigger Inputs

Each of Assimil8or’s 8 channels has a dedicated Gate/Trigger input with a trigger threshold of 1.6V. A rising edge at a Gate/Trigger input will initiate playback of the associated channel if the channel is in Master Mode and, depending on your preset, may trigger other channels in Link, Cycle or Stereo/Right Modes. (See the Channels chapter for details about Channel Modes.)

### Control Voltage Inputs

Assimil8or provides 24 CV inputs that can be arbitrarily assigned to any parameters on any channels. A single CV can be assigned to multiple parameters on multiple channels (although each individual parameter can only have one CV assigned to it).

The CV inputs accept voltages in the range of -5V to +5V, and voltages above or below this level are seen as +5.000V or -5.000V respectively.

Each Channel’s CV A input is sampled at 96kHz and anti-aliased down to a 20kHz bandwidth. CV B and CV C inputs are sampled at 48kHz and are not anti-aliased.

#### Relative vs. Absolute Modulation Assignments

When selecting a modulation source for a parameter, you will notice the the first 3 choices (after “Off”) are always CV A, CV B, and CV C, followed by all of the 24 inputs numbered: 1A, 1B, 1C, 2A, 2B,… etc.  The CV A, CV B, and CV C inputs are what we call “relative” inputs. The numbered inputs are “absolute” inputs. Here’s what that means:

CV A, CV B, and CV C always refer to the 3 physical inputs associated with the channel you’re editing. For example, if you’re editing Channel 2 of a preset and assign CV A to modulate pitch, the channel would look for a CV at the “A” jack of the second row of inputs.  If you then copied that channel to Channel 7, the channel would look for a CV at the “A” jack of the seventh row of inputs. The inputs are always relative to the physical channel.

If however, in the example above, when editing Channel 2, you assigned input 2A to modulate pitch, for that channel the result would be the same. It would still look for a CV at the “A” jack of the second row of inputs. But if you then copied that channel to Channel 7, that channel would still look for a CV at the “A” jack of the second row of inputs (i.e., 2A) as you would have assigned that absolute input.

## Outputs

### Individual Channel Outputs

Each of Assimil8or’s 8 channels has a dedicated individual output. Each channel’s signal always appears at its individual output (and may optionally appear at the Mix Outputs described below).

### Mix Outputs

Each channel can optionally be assigned to the Mix Outputs with a mix level and pan setting. The mix level is an offset (either higher or lower) based on the channel’s individual output level.

NOTE: Both the individual and mix outputs are active during the process of sampling, so channels may be played and resampled in real time.

A TIP: While the individual outputs are monophonic, since you can sample the mix output, you could create a submix to the mix output, sample it, and then have it available at one (if mono) or two (if stereo) individual outputs.

## Controls

### DATA 1 Encoder

The DATA 1 encoder is used to select and, with the DATA 2 knob, to set the value of various parameters (see the Setting Parameters section below). It also selects Folders, Channels, or Samples for loading.

The encoder includes an integrated pushbutton that is typically used to load the currently selected Folder, Channel, or Sample, to enter a currently selected parameter value (see individual parameters for details), or to confirm some action.

### DATA 2 Knob

The DATA 2 knob is used to set the
values of parameters.

Additionally, for real-time control, in each preset you can assign the DATA 2 knob to replace any one of the 24 CV inputs when you’re on the home preset screen. (Great for live performance.) Make the assignment at the bottom of the Channels page or by holding down the Play Mode button and turning DATA 2 while on the home page.  Any voltage at the assigned CV’s input jack is ignored.

### Setting Parameters

On each parameter screen, use the encoder to highlight a parameter and then use the DATA 2 knob to set its value. If you need a more precise setting, click the DATA 1 encoder to edit at the maximum resolution.  Click the encoder again to enter the selected value.

IMPORTANT NOTE: Whenever there are any unsaved parameter changes in a preset, a yellow warning sign will appear in the lower left-hand corner of the home display.  If you select a new preset before saving the current one, the changes will be lost.

### Channel Buttons 1-8

Pressing a Channel Button will trigger the associated channel and also select that channel for editing. The associated LED will light whenever the channel is triggered, whether via the button or via an external trigger or gate.

NOTE: If you want to select a channel for editing without triggering it (in a live performance, for example), press and hold the Channels/ Select button and press the desired channel button. The channel will be selected, but it will not be triggered.

ANOTHER NOTE: A channel button will always trigger the associated channel, even if the channel is in a mode (i.e., Link, Cycle, or Stereo/Right) that results in its getting triggered by another channel’s trigger.  This allows you to audition the channel during editing without interference from any associated channels. It will, however, also be triggered when you press the associated Master channel’s button.

### Load Button

This button allows you navigate the files on an inserted micro SD card. See Chapter 6 for details.

### Save Button

This button allows you to save presets to an inserted micro SD card. Presets are always saved to the currently loaded folder. Details in Chapter 6.

### Utility Button

Pressing this button brings up a menu where you will have access to Assimil8or’s various housekeeping and maintenance functions. See Chapter 21 for details.

### Channels/Select Button

Pressing this button brings up the Channels screen, where you configure your presets by assigning samples to the various channels and setting Channel Modes and Crossfade Groups. See Chapter 9 for details.

Additionally, pressing and holding this button and then pressing a Channel Button will select that channel for editing without triggering it.

### Zones/Select Button

Pressing this button brings up the Zones screen, where you can assign up to 8 samples to the current channel for selection under CV control, along with adjusting the CV voltage range for selecting each sample. See Chapter 10 for details.

Additionally, pressing and holding this button and then pressing a Channel Button will select the Zone whose number matches the Channel Button number. For example, if you are editing Channel 3, which has 8 zones assigned to it, and press and hold the Zone button and then press the Channel 5 button, you will select Zone 5 on Channel 3.

### Sample and Sampling Setup

These buttons allow you to set the various options involved in the sampling process and to initiate the actual sampling. See Chapter 7 for details.

## Channel Parameters

The following buttons each open a screen with one or more related parameters that affect the currently selected channel. They will be described in detail in their own chapters.

### Pitch

Lets you set the channel’s initial transposition (if any) and program linear and/ or exponential frequency modulation. Also lets you set a pitch offset for each zone in the channel.

### Level

Lets you set the channel’s initial level and program linear and/or exponential amplitude modulation. Also lets you set a level offset for each zone in the channel.

### Phase Modulation

Lets you select the phase modulation source (channel, sample input, or CV) and set the modulation index and any modulation index modulation (modulation modulation!).

Additionally, holding down this button and pressing any of the channel buttons causes that channel button to be “held down” (and its LED to flash) until the channel button is pressed again.

### Mutate

Provides a variety of functions that affect the channel’s audio quality. Includes the ability to modify the channel’s bit depth (from 1 to 32 bits, including fractional bits), to disable Assimil8or’s anti-aliasing technology, to reverse the channel’s audio, and to turn on or off Sample Smoothing, which minimizes artifacts from non-optimum loops, real-time zone switching, and sample re-attacks.

### Pan/Mix

Lets you set the channel’s level and pan in the mix output, set pan modulation, or remove the channel from the mix output altogether.

### Sample Start/End

Lets you set the points within a channel’s sample (or individually for its zones) at which playback starts and stops, as well as program modulation of the start and stop positions. Also lets you truncate the sample to the selected points and save the truncated sample as a new sample (leaving the original sample intact).

### Loop Start/End/Length

Lets you define a loop within a channel’s sample (or individually for its zones), as well as program modulation of the loop parameters.  Loops can be in Start/End mode (you independently define the loop start and end point) or Start/Length mode (you define the loop start and loop’s length).

The loop is turned on or off and its behavior is set by the Loop Mode button below.

### Play Mode/Latch

Selects 1 Shot Mode (a trigger or gate starts playback of the channel and the channel continues to play independent of trigger or gate length) or Gated Mode (the channel continues to play only as long as the gate is high).

### Envelope

Lets you set the attack and release times of the built-in envelope as well as set the modulation of those times. Also allows you to set the channel to Auto Mode, which causes the channel to automatically start playing as soon as its preset is loaded.

### Loop Mode

Lets you set the loop to Off, On (once in the loop the loop repeats indefinitely), or Gated (the loop repeats as long as the gate is high and continues into any remainder of the sample once the gate falls).

## Memory Card

Assimil8or can store and recall folders, presets and samples onto and from an inserted micro SD card. We’ve tested cards of up to 200GB is size, although there is no reason larger ones shouldn’t work as well.

A TIP: In addition to sampling directly into Assimil8or, you can also use your computer to create folders at the root level of your SD card and put WAV files in those folders. (Assimil8or is compatible with 8, 16, 24, or 32 bit integer mono or stereo WAV files at any sample rate.) While sample names may be up to 47 characters long, we recommend that both folder and sample names be both relatively short and descriptive. Trust us, it really makes things easier when you’re working with them on your Assimil8or.

IMPORTANT NOTE: There are a lot of squirrely cheap micro SD cards out there.

There are also cards that appear to be from major suppliers that are actually counterfeit.  While many cheap cards may be fine, we’d recommend that, for the security of your data, you use cards from known reliable manufacturers purchased from trusted sources.

# 5. The Main Display

Assimil8or’s main display provides an overview of the currently selected preset, along with some basic indication of what’s happening in the module. Additionally, there are dedicated displays for loading and saving presets, programing channel parameters, and executing utility functions.

In this chapter, we’ll describe the main display. The rest will be described in their own chapters.

IMPORTANT: OLED displays (which is
what the Assimil8or display is) have long

lifetimes under normal use, but if you leave your system on 24/7 (or just want to ensure the longest possible life for your display), Assimil8or provides the ability to adjust the brightness of the display (which is also useful for optimizing it for the ambient lighting level of your work environment) and, optionally, to set a time after which the display enters a screensaver mode. Both of these can help extend the life of your display. They are set in the Utilities menu. Details for setting them will be found in Chapter 21.

The main display provides the following:

### Left and Right VU Meters

These display an indication of the left and right channel levels at the MIX output.

### The Number and Name of the Currently Selected Preset

### 8 Channel Status Displays

For each channel, there is a display of:

- The channel number (if a sample or zones are assigned to that channel)
- If the number is black on a bright red background, that channel contains a sample and is selected for editing.
- If the number is black on a dimmer red background, that channel’s sample is loaded, but not selected for editing.
- If instead of a number, there is a red dot in the number field and a sample name in the sample field, there is a sample assigned to that channel, but it has not yet finished loading into memory.
- If there is a red dot in the number field and no sample name in the sample field, there is no sample assigned to that channel.
- If there is a red dot in the number field with a bright red frame around it, that channel is selected, but there is no sample assigned to the channel.
- 3 tiny CV indicators that show the CV level at that channel’s CV A, CV B, and CV C inputs.

NOTE: The channel may have additional CVs modulating parameters beyond those three.

- The name of the sample assigned to that channel or, if zones are assigned, the name of the sample in Zone 1.

NOTE: The sample name display is limited to 6 letters. If the sample name is longer than that, the remaining letters are not displayed here. For that reason, it’s usually a good idea to name your samples such that the first 6 letters are descriptive enough for you to recognize the sample from them.

### Waveform Display

A real-time display of the waveform of the currently selected channel. Only appears when the channel is actually playing.

### Yellow “Unsaved Changes” Indicator

When the little yellow caution triangle appears in the lower lefthand corner of the display, it indicates that you have made changes to the current preset that have not been saved. If you select another preset or load a new folder before saving the current preset, your changes will be lost.

### Folder Name

The name of the currently loaded folder appears at the bottom of the display.

### DATA 2 CV

The CV for which the DATA 2 knob is currently substituting (if any) is displayed in the lower righthand corner of the display. You can change the assigned CV from this screen by holding down the Play Mode button and turning the DATA 2 knob. An edit field will pop up allowing you to select the desired CV (or turn the function off).

# 6. Managing SD Cards, Folders, Presets, and Samples

## File Organization

Assimil8or’s files are organized in the following hierarchy:

### Micro SD Card

Assimil8or’s front panel micro SD card stores all of the folders containing the files required to play your stored presets. The card is strictly a storage medium. Audio is never played directly from the card.

### Folders

An Assimil8or SD card contains one or more folders. Each folder contains one or more presets and all of the presets’ samples.  Each folder may contain up to 199 presets (memory allowing).

Additionally, a folder may contain one or more samples not used in any of the folder’s presets.

### Presets

A preset contains all of the information necessary to play up to 8 programmed channels.

### Channels

A channel contains the information necessary to play one of Assimil8or’s 8 channels.

### Samples

Samples are the actual WAV files that contain the audio or control voltages that are the raw material for your channels.

NOTE: When scrolling through samples and folders on various screens, the order in which the samples and/or folders appear can be unpredictable. We’re currently evaluating whether we can make this better. If so, there will be a software update.

## Micro SD Card

The micro SD card is essentially a library of folders you’ve created (along with a few housekeeping files you don’t really need to worry about). Content may either be written directly to the card by your Assimil8or or, in the case of folders and WAV files, copied to the card from a computer.

All preset and sample files on the card are stored in folders at the root level of your card.  No nested folders.

If you’re copying files from a computer, create a folder on your SD card and give it a descriptive name. Put the WAV files (also descriptively named) you’ll want for your preset(s) into the folder, keeping in mind that Assimil8or has 422MB of sample memory.  Assimil8or is compatible with 8, 16, 24, or 32 bit integer mono or stereo WAV files at any sample rate.

WARNING: It’s an extremely unwise idea to remove an SD card while Assimil8or is executing any load, save, or browse function.  Or, in fact, any function that might even possibly require accessing the card (formatting is an obvious example). Seriously, just don’t do it.

IMPORTANT NOTE: As mentioned in Chapter 4 (but it’s worth mentioning again), there are a lot of squirrelly cheap micro SD cards out there. There are also cards that appear to be from major suppliers that are actually counterfeit. While many cheap cards may be fine, we’d recommend that, for the security of your data, you use cards from known reliable manufacturers purchased from trusted sources.

## Folders

Folders are Assimil8or’s file storage construct.  Assimil8or can have one folder at a time in its memory. That folder contains a number of presets and all of the samples necessary to play those presets. It may also contain samples not used in any presets (if, for example, you placed samples in the folder from a computer or sampled multiple sounds or CVs into the folder, but have not assigned them to any preset).

NOTE: Although only one folder at a time may be in Assimil8or’s memory, when creating presets, you can import channels or samples from other folders on your SD card into your current folder. See the chapters on Channels and Zones for details.

## Loading Folders

To load a folder into your Assimil8or, press the LOAD button and use the encoder to scroll through the folders on your card.  When you’ve highlighted the desired folder, click the encoder to load the folder’s presets and the samples used in the presets. You will immediately be transferred to the main home screen while the folder loads.

### On-Demand Loading

Loading a folder into your Assimil8or uses a process we call “On-Demand Loading.” Its intent is to manage the loading of samples such that you can start playing your presets as soon as possible.

Here’s what happens when you click the encoder to load a folder:

- Assimil8or starts by loading the preset data for all presets in the folder, along with the headers (but not the audio data) for all the samples in the folder, whether used in a preset or not. While this is happening, you will see a green progress bar across the middle of the home screen that indicates the loading process. (If the folder contains only a few presets and/or samples, the progress bar may barely flash on the screen.)
- Once the preset data and sample headers have been loaded, Assimil8or selects the lowest numbered preset in the folder as the current preset and starts loading the samples used in that preset. You will see a green progress bar along the top of the display that will indicate the load process of each sample. As each channel is loaded, its channel number will appear in its number field in the main display and that channel becomes immediately playable.
- Once all of the samples of the first preset are loaded, Assimil8or continues through the remaining presets in numerical order until every preset’s samples are loaded.  Unassigned samples are not loaded.
- However, if, while presets are loading, you to scroll to a preset that is beyond the currently loaded presets and select it, Assimil8or completes the loading of any channel that it was in the midst of loading and then jumps to your selected preset and begins loading its samples. After loading that preset, it continues loading the numerically higher presets, and then circles back to load any presets that it had jumped over to get to your selected preset.

#### At this point, an example is probably in order

 1. You load a folder with Presets 001-010.  Immediately the samples of Preset 001 begin loading.
 2. Once it’s loaded, you start playing channels of Preset 001 while Assimil8or starts loading the samples of Preset 002.
 3. Before Preset 002 is completely loaded, you scroll to Preset 007 and select it.
 4. As soon as Assimil8or completes loading whichever channel of Preset 002 it was loading when you selected Preset 007, it immediately starts loading the samples of Preset 007.
 5. Once finished loading Preset 007,

Assimil8or continues to load Presets 008, 009, and 010 and then circles back to Preset 002 to complete its loading, followed by Presets 003-006.

### What about those unassigned samples?

Unassigned samples remain unloaded until you decide to assign them to a channel or zone in a preset you’re programming.  They load at that point. See the chapters on Channels and Zones for details.

## Presets

A preset contains the information necessary to play up to 8 of Assimil8or’s channels with the parameters you’ve programmed. Presets are always contained in folders, along with their required samples. When examining the contents of an SD card on your computer, the preset files have a .yml suffix.

> NOTE: Presets files are saved in the YAML format. Since YAML is human readable, you could, if you wanted, open a preset file in a text editor and examine, or even modify it. (Keep in mind that you could mess up your presets pretty majorly this way.) On the other hand, someone with the appropriate skills could, if so inclined, create a computer-based preset editor that generated YAML files that could then be copied onto an SD card. Just sayin’.

We’ll be publishing the YAML preset file format in the not-too-distant future for anyone so interested.

### Loading Presets

In the home screen, turn the encoder to scroll through all existing presets. When you see the one you want, click the encoder’s switch.

If you press and hold the encoder switch and then turn the encoder, each preset will load immediately as you scroll to it.

> IMPORTANT NOTE: Once you’ve loaded a folder and all of its headers have been loaded into memory, you can immediately select any of the folder’s presets. However, if the folder and/or the preset contains one or more long samples, it may be the case that the sample(s) have not yet been completely loaded into memory. This is indicated by a red dot on the home page next to one or more channel names. Once a sample is completely loaded, the dot will change to the channel number.

> ANOTHER NOTE: Channels in presets become immediately playable as soon as their sample(s) load, even if other channels in the preset are still loading. This may or may not be useful to you, depending on your situation.

### Importing Presets

You can import presets from other folders on your SD card into your current folder, in which case the preset’s sample(s) are also imported into the current folder.

#### To import a preset

  1. While in the destination folder (i.e., the folder you want to import the preset into), press the LOAD button.
  2. Scroll to the Folder on your SD card that contains the preset you want to import.
  3. Double-click the LOAD button to display the contents of the selected folder.
  4. Scroll through the folder’s contents to locate the preset you want to import.
  5. Click the encoder to bring up the File Op window. Select “Import” and click the encoder again.
  6. The preset and all of its samples will be imported into your initial folder and you will be returned to that folder with your imported preset selected.

### Starting with an Empty Preset

When creating presets, you may sometimes want to start out with a completely empty preset. When starting in a folder with no previously saved presets, you can start with the default “empty” preset. But once a preset has been saved in a folder, turning the encoder only lets you access previously saved presets.

To start with an empty preset in this situation, press the encoder’s switch and, while holding it pressed, turn the encoder. This will allow you to access all 199 of a folder’s potential presets, whether empty or not. Select an empty one and start programming.

### Saving Presets

Press the Save button to bring up the Save Preset field. The current preset is initially displayed.

### Selecting a Location

In the Save Preset field, the encoder initially controls the Preset Number field. Scroll through the numbers to select a destination location (or don’t scroll to resave to the current preset’s existing location). Note that this scrolling does include empty (“New”) preset locations. At the top of the scrolling list is a special item, **ERASE**.

### Saving Without Changing the Name

To save the current preset to the selected location without changing the location’s existing name, either press the encoder for 2 seconds, or press the Save button for 2 seconds. The display briefly displays “Saving in 2 Seconds…” and then (after 2 seconds) displays “Save Completed” and exits the Save Preset screen.

If you release the button before 2 seconds have elapsed, the display briefly shows “Save canceled” and exits the screen without executing the save operation.

NOTE: The Save Preset operation can also be exited at any time without saving by pressing any other function buttons.

### Changing the Preset Name

To change the name of the preset at the selected target location, press the encoder.  A cursor will highlight the first character in the Name field.  (If the selected location was

NEW, the Name field will change to the name of the current preset.)

The name is changed using the encoder as follows:

  1. After a highlighted character has been selected using the encoder, either select the new character using DATA 2 or click the encoder to select the new character.
  2. If you’ve used the encoder to select the character, click the encoder to enter that character and return the encoder to character location selection operation.
  3. If you’ve only used DATA 2 to select the character, simply turn the encoder to highlight the next character you want to change.
  4. Repeat as necessary.

### Saving After a Name Change

To save the renamed preset to the selected location, either long press the encoder, or long press the Save button. This can be done while either in the character location selection or character changing operation for the encoder. The display briefly displays “Saving in 2 Seconds…” and then (after 2 seconds) displays “Save Completed” and exits the Save Filter screen. If you release the button before 2 seconds have elapsed,the display briefly shows “Save canceled” and exits the screen without executing the save operation.

### Erasing the Current Preset

To erase a preset, press Save and then scroll to the beginning of the menu to display

**ERASE**
(where ### is the preset number of the current preset which will be erased). While **ERASE** is displayed, either long press the Encoder, or long press the Save button. The display will briefly display Erasing Preset and then exit the screen. If you release the button while Erasing Preset is displayed, the display briefly shows Erase canceled and exits the screen without executing the erase operation.

## Channels

Each channel contains the information required to play your programmed audio or CV files through it’s dedicated channel output and, optionally, through the mix outputs. A channel plays either one sample or, if you are using the Zones function, up to 8 samples that can be selected by a CV. Channels are configured, appropriately enough, on the Channels screen and, optionally, the Zones screen.

Channels can be assigned a variety of modes that allow them to interact with other channels in your preset in many creative ways. Details will be found in the Channels chapter.

### Channel Parameters

The following parameters are referred to as Channel Parameters, because while they affect a channel’s sample(s), they are actually owned by the channel, not the sample. If you set up a channel and then replace the sample in the channel with another, the new sample inherits all of the parameter values of the initial sample.

Channel parameters include: Pitch, Level, Phase Mod, Mutate, Pan/Mix, Sample Start/ End, Loop Start/End/Length, Play Mode, Envelope, and Loop Mode.

### Copying and Importing Channels

Once you have created a channel, you can copy it to other channels in your preset or to channels in other presets in the current folder. Additionally, you can import channels from other folders on your SD card into channels in the current folder, in which case the channel’s sample(s) are also imported into the current folder. Again, see the Channels chapter for details.

## Samples

Samples are the raw material of your channels and presets. Samples can be recorded directly by Assimil8or or can be copied onto an SD card via computer.

See the Sampling chapter for details of Assimil8or’s sampling options.

To use your computer to load existing WAV files, create folders at the root level of your SD card and put the WAV files in those folders. Assimil8or is compatible with 8, 16, 24, or 32 bit integer mono or stereo WAV files at any sample rate. While sample names may be up to 47 characters long, we recommend that both folder and sample names be both relatively short and descriptive.

> IMPORTANT NOTE: Do NOT click the encoder here. If you do, you will actually load the folder (rather than browse its contents) and erase any unsaved changes in the preset you were working on.

- Scroll through the folder’s contents to locate the sample you want to import.
- Click the encoder to bring up the File Op window. Select “Import” and click the encoder again.
- The sample will be imported into your selected channel or zone and you will be returned to your current preset with your imported sample in place.

### Renaming and Erasing Samples

To rename a sample or to erase a sample from the current folder (and from the inserted SD card), on either the Channels or Zones page, highlight the sample and click the encoder to bring up the Sample Selection field. Then long-press the encoder switch to bring up the Sample Op window and select Rename or Erase as desired and click the encoder again. Proceed with renaming or erasing.

> NOTE: Erasing a sample will delete it from every preset it appears in, so make sure you know where it’s used before deleting it, as the deletion is permanent.

### Importing Samples

When creating presets, samples must be in the currently loaded folder in order to be assigned to channels or zones. However, samples can be imported from other folders into the currently loaded one.

#### To import a sample

- With the destination channel or zone selected (i.e., the channel or zone you want to import the sample into), press the LOAD button.
- Scroll to the Folder on your SD card that contains the sample you want to import.
- Double-click the LOAD button to display the contents of the selected folder.

# 7. Sampling

The Sampling Setup screen lets you configure Assimil8or’s sampling functions.  Once configured, you can choose to trigger sampling manually with the Sample button, automatically when the incoming signal exceeds a programmable threshold level, or under the control of a CV input.

NOTE: One of Assimil8or’s key characteristics is that the module is otherwise functional during the sampling process, so you can not only resample whatever it’s playing, you can trigger channels or modify what it’s playing (by changing parameters) while it’s sampling.

## Basic Sampling Process

The basic process for recording a sample is:

 1. Connect the signal source(s) to one or both of the Sample Inputs
 2. Press the Sampling Setup button to bring up the Sampling Setup screen
 3. Set all of the parameters on the screen as second time desired.
 4. Play your audio and adjust the sampling level
 5. If you are going to use Threshold triggered sampling, adjust the threshold level.
 6. If you are going to use CV triggered sampling, assign the desired CV input.
 7. Unless you’re already in HOT mode (see the Arming Safety section below), press and hold the Sampling Setup button to arm sampling. The Sample LED will flash and the message “SAMPLING ARMED” will appear at the top of the screen.

> NOTE: You can long-press the Sampling Setup button to arm sampling from any screen. You do not have to be on the Sampling Setup screen.

8. Once armed, sampling can be triggered by pushing the Sample button, having the incoming audio exceed the programmed threshold level, or in response to the selected CV exceeding 1.6 volts
9. Sampling will stop when either:

- The preset sampling time has elapsed
- The sample memory is filled
- You press the Sample button a second time
- The selected CV rises above 1.6 volts for a second time

 10. Once sampling has stopped, opening the Sampling Setup screen (if you’re not already on it) will display an edit field that will give you the option of keeping or deleting the sample you just recorded.  That field will be available on the screen for 30 seconds after sampling ends. If you know you’re not going to want to keep the sample, you can delete it here. If you know you want to keep it, or are not yet sure, keep it for now.

> NOTE: If you don’t make a choice in this edit field for 30 seconds, the sample will automatically be kept.

## Sampling Setup

The Sampling Setup screen is where you configure the sampling process.

Down the right hand portion of the screen are the main configuration settings.

They are, in order:

### Destination

Destination lets you specify where the sample(s) you are about to make will end up. The choices are:

#### Unassigned

The sample will appear in the current folder, but will not be assigned to any preset. You will not be able to audition the sample until you have assigned it to a channel. You might select Unassigned if you were sampling many files in succession and didn’t need to go back and listen to them until you had finished, at which time you could assign them one at a time to a single channel to audition them.

#### Channel 1-8

Assigns the sample to the specified channel in the current preset.  This setting will cause the new sample to replace whatever was previously assigned to the channel.

#### Empty Channel

Assigns the sample to the lowest numbered empty channel in the current preset. Useful if you are sampling a series of sounds to fill the current preset, as you won’t have to change the destination after every sample.

> NOTE: If you select Empty Channel and no channel is empty, your sample will be assigned to the Unassigned pool.

### Record Mode

There are two record modes, Once and Circular. Here’s how they work:

#### Once

With Once selected, Assimil8or will sample for the time set in the Sampling Time parameter below and then stop (if you haven’t already manually stopped first). If you stop sampling before the selected length, the sample is truncated to your stop point.

#### Circular

With Circular sampling, Assimil8or samples for the time set in the Sampling Time parameter below and then circles back to the start of sample and continues sampling, writing over what was previously sampled as it proceeds.  It continues doing this until stopped manually or via CV control.

If you stop sampling before the selected length (i.e., before it cycles back for the first time), the sample is truncated to your stop point, just as it would be with Once above.

If you stop sampling after sampling has cycled back at least once, you will get your recording of the entire programmed sampling time.

### Sampling Time

This parameter lets you set the maximum sampling time for your sample.  The choices are “All” (i.e., all of the currently available memory in the current folder) and absolute times that range from 0.1 second to 600.0 seconds in .1 second intervals.

> NOTE: This setting represents the maximum sampling time for your sample.

If you stop the sampling process before all of the set time has elapsed, your sample will be truncated to the time actually used by the sample.

### Sampling Rate

This parameter sets the sampling rate for your sample.  Choices are 48kHz, 96kHz, and 192kHz.  As you would expect, each higher sampling rate uses twice the amount of memory for the same sampling time as the rate below it.

> A TIP: For most samples not intended specifically for dogs, the lower sampling rates definitely make more efficient use of memory with little or no sonic compromise.  However, if you are sampling something with substantial super high frequency content and you know you’ll want to be pitch shifting it down (which can give some very interesting effects), the higher rates may be the way to go.

### Naming Mode

When you record a new sample, it is initially given a default name (which you would do well to change to something more useful at some point - some point soon). This setting lets you specify the default naming scheme. The choices are:

#### New001

Each new sample is named New###, where ### is a number that starts at 001 and increments 1 for each new sample. So, New001, New002, New003, etc.

#### Pnm001

Each new sample is named ???###, where ??? Is the first three letters of the current preset name and ### is a number that starts at 001 and increments 1 for each new sample. So if you had selected a preset called “Snares,” new samples would be Sna001, Sna002, Sna003, etc.

#### S001

Each new sample is named S###, where ### is a number that starts at 001 and increments 1 for each new sample.  So, S001, S002, S003, etc.

### High Pass Filter

This setting allows you to decide if you want your sample to be AC or DC coupled. If you are sampling CVs, you definitely want DC coupling.

If you are sampling audio and you know (or suspect) that the audio has an unwanted DC component, select AC coupling.

> NOTE: When sampling CVs, it should be noted that while the sampling accuracy is sufficient for virtually any sort of modulation shapes (envelopes, LFOs, etc.), it is not designed to record 1V/oct pitch CVs with sufficient audio path gain accuracy to provide precision chromatic note values.  If you want to do this, you will need to manually tweak the gain for your particular patch.

### Arming Safety

This parameter lets you choose whether or not you will need to manually arm sampling before each sample is made, or whether sampling can always be immediately initiated by manual button press or CV.

To always require arming, select “Safe.” To allow immediate triggering, select “*HOT*.”

> NOTE: Threshold triggered sampling always requires arming, regardless of the Arming Safety setting.

> ANOTHER NOTE: Unless you have a specific reason to work in HOT mode (e.g., sequential sampling in a live situation where you don’t have control of the signals being sampled and need to be sampling on the fly), we recommend that you stay in Safe mode. We can’t tell you how many annoying times we accidentally triggered sampling before implementing Safe mode.

### Level

Level lets you adjust the level of the incoming signal from -30dB to +24dB. In addition to the numeric field, there is a blue graphic indicator of the level value. Additionally, playing your signal into the sample input will display the resulting level on the yellow meter. Your goal is to set a level that results in a nice hot level on the yellow meter without ever clipping it at 0dB.

### Side

This parameter tells Assimil8or where to look for the incoming signal(s) and what to do with them. Choices are:

#### Left

A mono signal coming into the left sample input. The sample is stored as a mono sample.

#### Right

A mono signal coming into the right sample input. The sample is stored as a mono sample.

#### Stereo

A stereo signal coming into the left and right inputs. The sample is stored as a stereo sample.

#### Dual Mono

Two otherwise unrelated mono signals coming into the left and right inputs. The sample is stored as two independent mono samples.

### Threshold and CV Trigger Assign

This parameter lets you set the threshold level which, if exceeded by the incoming signal, will trigger sampling. Alternatively, it lets you select a CV input to trigger and stop sampling.

#### Threshold

To set the threshold level, highlight the edit field and use DATA2 to adjust the level, observing the arrow indicator to set the level at an appropriate value relative to the level of the incoming audio. (You could use the encoder, but then you wouldn’t see the cute little arrow indicator move in real time.)

The threshold level is adjustable from -60dB to -1dB.

If you continue adjusting the value past -1dB, you will encounter “Off,” which turns off threshold triggering.

If you continue adjusting beyond “Off,” you will be able to choose any of the 24 CV inputs to act as a sampling trigger.

> NOTE: The different triggering methods can be used in combination to start and stop sampling. For example, you could start sampling with the Sample button and stop it with the CV (or the reverse). If you start it via the Threshold, you will have to stop it with the Sample button or simply let it complete the preset sampling time.

# 8. Sample Start and End

## Sample Start

Sample Start sets the point at which the sample starts playing when its channel receives a trigger or gate. The position of the start point can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter. Positive CVs move the start point towards the end of the sample, while negative CVs move it toward the beginning of the sample. Modulation gain can be set over a range of from -1.00 to +1.00.

> NOTE: Sample start position is read each time the channel receives a trigger.  Moving the start point, either manually or via modulation, while a sample is playing will have no effect until the next time the channel is triggered.

> ANOTHER NOTE: Changing the sample start point is nondestructive. It does not affect your sample’s data. If you want to permanently remove data from the beginning of your sample, see the Permanent Truncation section below.

> YET ANOTHER NOTE: You can never move the start beyond the current position of the end point, either manually or via modulation.

> AND EVEN ANOTHER NOTE: Keep in mind that setting the start point (or modulating the start point) in a non-silent portion of the sample will almost certainly cause a click if the envelope is set to a fast attack. If you don’t want a click, either don’t do that, or set the envelope to a more gradual attack.

## Sample Start and End

This screen lets you set the point at which your sample starts playing when it receives a trigger and the point at which it stops playing.

### About the Display

In addition to the numerical positions (in samples) of the Start and End points, the screen also includes a graphical waveform display of the entire sample, as well as a high resolution display of the region around the point being adjusted. The high resolution display provides individual sample resolution.

In both displays, the start point marker is green and the end point marker is red. If the channel has been reversed, the waveform display shows a red border to remind you of that fact.

When adjusting either point, use the DATA 2 knob to get in the general neighborhood of where you’d like it to be. If you then highlight the appropriate numerical field and click the encoder to bring up the editing field, you can adjust the point in single sample increments.

> NOTE: You can bring up the screen by pressing either the Sample Start or Sample End button. The screen will appear with the selected numerical field highlighted.  Once the screen is displayed, you can use the two buttons to switch back and forth between the two points for editing. (You can, of course, also use the encoder to navigate to either field.) If you press either button twice in succession, you will dismiss the screen.

### Sample End

Sample End sets the point at which the sample stops playing (assuming a loop isn’t set in the sample that prevents the sample from ever getting to the end point). The position of the end point can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter.  Positive CVs move the point towards the end of the sample, while negative CVs move it toward the beginning of the sample.  Modulation gain can be set over a range of from -1.00 to +1.00.

> NOTE: You can move the end point, either manually or via modulation, while a sample is playing, but once the sample encounters the end point, the sample will stop playing and any additional end point adjustment will have no effect until the channel is subsequently re-triggered.

> ANOTHER NOTE: Changing the end point is nondestructive. It does not affect your sample’s data. If you want to permanently remove data from the end of your sample, see the Permanent Truncation section below.

> YET ANOTHER NOTE: You can never move the end point before the current position of the start point, either manually or via modulation.

> AND EVEN ANOTHER NOTE: The sample end always smooths the transition to silence, so no sharp click is heard.

### Zones

If a channel is using the Zones function, the start and end points can be set independently for each sample in a zone. Simply select each zone and adjust its settings.

To select a zone, press and hold the Zones/ Select button and then press the Channel Button whose number matches the desired zone.

The number of the currently selected zone is displayed in the upper righthand corner of the screen, along with the number of the currently playing zone (in red). It is possible for these to be different, so if you’re setting a zone’s start and end points and don’t hear any effect, make sure the zone you’re hearing is the one you’re actually editing.

### Permanent Truncation

As mentioned above, setting start and end points does not affect your sample’s data.  However, if you do want to discard the actual data before the start point and/or after the end point (to free up unneeded memory, for example), you can use the Truncation function to create a new sample that contains only the data between the start and end points.

> NOTE: Truncation does not affect your original sample. It creates a new sample with the suffix “T00.” So, if you start with a sample called Snare1 and truncate it, Snare1 still exists unedited, but a new sample named Snare1T00 is created. If you then further truncate Snare1T00, a new sample named Snare1T01 his created. You can probably see where this is going.

To truncate the beginning of the sample (the data before the currently set start point), set the start point as desired and then press and hold the Sample Start button. The display will show “Truncating in 2 seconds.” If you release the button before the 2 seconds have elapsed, the truncation will be canceled. If you hold it for the required 2 seconds, the display will show “Sample saved” and your new truncated sample will be selected.

To truncate the end of the sample (the data after the currently set end point), set the end point as desired and then press and hold the Sample End button. As above, the display will show “Truncating in 2 seconds.” If you release the button before the 2 seconds have elapsed, the truncation will be canceled. If you hold it for the required 2 seconds, the display will show “Sample saved” and your new truncated sample will be selected.

If you wish to truncate both the beginning and end at once, set the start and end points and then press both the Sample Start and Sample End buttons simultaneously. As above, the sample will be truncated after 2 seconds and the new truncated sample will be selected.

> NOTE: When you truncate a sample in a channel or zone, the channel or zone will now use the truncated sample (i.e., the truncated sample replaces the original in your channel zone). However, if the original sample is used in any other channels or zones, it will not be automatically replaced in those. If you want to use the truncated sample in those channels or zones, you will need to replace them manually.

Once you’ve created a truncated sample, you can, if you’re sure you’ll never again want the original sample, go back and erase the it.

# 9. Channels

The Channels screen (along with the Zones screen, if you’re using zones) is where you configure your presets, assigning samples to channels and setting Channel Modes that define the way that channels interact with other channels. Additionally, this is one of the two places (along with the main home screen) where you can select the CV input that you’d like the DATA 2 knob to replace when on the home screen.

> IMPORTANT NOTE: It’s important to understand that channel parameters (Pitch, Level, Phase Mod, Mutate, Pan/Mix, Sample Start/End, Loop Start/End/Length, Play Mode, Envelope, and Loop Mode), while they affect a channel’s sample(s), are actually owned by the channel, not the sample. If you set up a channel and then replace the sample in the channel with another, the new sample inherits all of the parameter values of the initial sample.

> A FURTHER IMPORTANT NOTE: Expanding on the above, the Loop parameters in particular will almost certainly need to be re- adjusted for any replacement sample.

Consequently, when replacing samples in existing channels, you may (or may not) need to adjust those parameters as desired.

### The Channels Screen

For each of the 8 channels, the Channels screen includes:

#### A Channel Number Area

If the channel has a sample assigned to it, the channel number will be black on a red background. If the channel has been selected, either by having its channel button pressed or by being highlighted by the encoder, the red background will be brighter to indicate its selection.

If a channel does not have a sample assigned to it, there will simply be a red dot in its number area.

#### Assigned Sample Name

This field contains the name of the sample assigned to that channel. If the channel uses zones, this will be the name of the sample assigned to Zone 1.

#### Channel Mode (MD)

Channel Modes offer a variety of ways for your channels to interact to create unique textures and effects. They are described below.

#### Crossfade Group (X)

Crossfade Groups let you assign from 2 to 8 channels to groups which can then be crossfaded under CV control with variable crossfade width. Up to 4 Crossfade Groups may be defined and independently controlled. The controlling CV input and the crossfade width for each group are set in the fields at the bottom of the screen.

### Assigning Samples to Channels

The most basic function of the Channels screen is to let you assign samples to channels. To assign a sample to a channel, highlight the Assigned Sample field and click the encoder. The Select Sample window will appear. Scroll to the sample of your choice and click the encoder again to select it.

> NOTE: If the sample you assign has been used in another preset in your folder, it will already be present in memory, so will be immediately available to play. However, if the sample has not been used in another preset, it will first have to be loaded into memory from your SD card. If it’s a short sample, you probably won’t even notice the delay. But if it’s a long sample, you may have to wait for a bit.  You can refer to the progress bar at the top of the display for load status.

> ANOTHER NOTE: If a channel is using zones, the Assigned Sample field will show the name of the sample in Zone 1. If you replace or delete this sample in the Channels screen, the sample will be replaced or deleted from Zone 1 in the Zones screen.

### Importing Samples

When selecting a sample for a channel, you can also import samples from other folders on the currently inserted SD card.  See Chapter 6 for details on importing samples.

> NOTE: As mentioned above, if you replace an existing sample with a different sample, the new sample will inherit all of the channel’s channel parameters that had been set for the previous sample. You may (or may not) need to adjust those as desired.

### Copying Channels

If you’ve previously programmed a channel (either in the current preset or in another preset in the current folder) that you would like to copy into a channel in the currently selected preset, highlight the destination channel’s assigned sample field and long press the encoder switch. This will bring up the Copy Channel field. Scroll to the channel that you’d like to copy into the selected channel and click the encoder.

### Importing Channels

Like importing samples from other folders as described above, you can also import entire channels from presets in other folders on your SD card. Here’s how:

  1. With the destination channel selected (i.e., the channel you want to import the new channel into), press the LOAD button.
  2. Scroll to the folder on your SD card that contains the preset that contains the channel you want to import.
  3. Double-click the LOAD button to display the contents of the selected folder.
  4. Scroll through the folder’s contents to locate the preset with the desired channel.
  5. Double-click the LOAD button again to display the preset’s channels. Scroll to the channel you want to import.
  6. Click the encoder to bring up the Channel Op window. Select “Import” and click the encoder again.
  7. The Channel and all of its samples will be imported into your initial preset and you will be returned to that preset with your imported channel selected.

### Copying or Importing Channels vs Replacing or Importing Samples

An important distinction to keep in mind is the difference between replacing or importing a sample into an existing channel vs copying or importing a channel into that same channel.

When you copy or import a sample into a channel, that sample will be affected by all of the channel parameters that were previously programmed for that channel.  Those parameter values may or may not be appropriate to the new sample.

When you copy or import a channel into an existing channel, the new channel brings its sample(s) along with all of the channel parameter values programmed for that channel. Consequently, one can assume that those values are appropriate for the sample and the channel’s intended effect (which is presumably why you’d be copying or importing the channel in the first place).

### Channel Modes

Channel modes are selected in the channel’s MD field. The channel modes are:

#### Master

A Master channel is a basic channel that gets its trigger from its associated Gate/Trigger input. If your preset is configured simply as 8 (or fewer) completely independent channels, each with its own trigger and modulation routings, set each of them as a Master channel and you’re done.

> NOTE: As you will see below, a Master channel can interact with other channels, depending on those channels’ own Channel Modes.

#### Link

Link Mode is designed to let you create layered voices. A channel in Link Mode does not respond to its own channel’s trigger, but instead is triggered by the trigger or gate of the Master channel in closest proximity above it.

Multiple Link channels can be triggered by
one Master, so you can build layered voices
of up to 8 layers.

You can have multiple linked groups in a single preset. For example, the following configuration would give you 1 four-layer voice and 2 independent two-layer voices:

 1. Master
 2. Link
 3. Link
 4. Link
 5. Master
 6. Link
 7. Master
 8. Link

For an example of Links, check out the Demo-Link folder in the sample sounds.

#### Stereo/Right

The Stereo/Right Mode is intended primarily (but not necessarily exclusively) for stereo samples. A Stereo/ Right channel inherits the trigger/gate and channel parameters (except for pan) of the Master channel above it. So, typically, for a stereo sample, you’d assign the left channel to Master mode and the right channel to Stereo/Right Mode.

Pan is not included in the shared parameters to allow you to independently set the pan positions of the two stereo channels.

> NOTE: All channel parameter values programmed in the Stereo/Right channel are ignored, but are still saved with the channel. If the channel is later changed to a different mode, those parameter settings would then become active.

#### Cycle

Cycle Mode is designed to allow a single trigger source to trigger multiple channels in sequence. A Master channel’s trigger/gate will sequentially trigger the Master and each of the Cycle Mode channels below it in order (until another Master channel is encountered), cycling back to the Master after the last Cycle Mode channel and continuing the cycle as long as triggers are received.

Assigning the same sample (e.g., a ride cymbal) to these channels lets their releases overlap naturally on repeated retriggering rather than cutting off unnaturally with each new attack. Assigning different samples to the cycling channels allows a variety of potentially interesting rhythmic effects.

As with Link Channels above, you can have multiple cycling groups in a single preset.

The following configuration, for example, would give you two 3-channel cycling groups and a 2-channel link group:

 1. Master
 2. Cycle
 3. Cycle
 4. Master
 5. Cycle
 6. Cycle
 7. Master
 8. Link

For an example of Cycles, check out the Demo-Cycle folder on your SD card.

### Combining Channel Modes

The various Channel Modes can be interspersed for interesting effects. For example, in the following configuration, the three Link groups alternate being triggered in Cycle Mode:

 1. Master
 2. Link
 3. Link
 4. Cycle
 5. Link
 6. Link
 7. Cycle
 8. Link

Here are 4 stereo samples being cycled (the Cycle Mode channels are the left channels of the stereo samples):

 1. Master
 2. Stereo/Right
 3. Cycle
 4. Stereo/Right
 5. Cycle
 6. Stereo/Right
 7. Cycle
 8. Stereo/Right

### Crossfade Groups

Crossfade Groups let you assign from 2 to 8 channels to groups which can then be crossfaded under CV control with variable crossfade width. Up to 4 Crossfade Groups may be defined and independently controlled.

To assign a channel to a Crossfade Group, navigate to that channel’s “X” field and select from group A, B, C, or D. Continue assigning channels to the selected group as desired.  You can then assign a CV to control the crossfade and set the width of the crossfade.  Those settings are made at the bottom of the Channels page. Either navigate to those fields and press a channel button to select the group to program, or highlight a channel’s group letter and long-press the encoder to jump to the XF field with that channel already selected.

The **Crossfade Width** parameter varies from 0.01 to 10.0 volts and controls the width of the crossfades between the group members. A small value will result in very short transitions, while large values will provide gradual transitions that will result in multiple members of the group being audible simultaneously. Experimentation is the key.

Channels in a Crossfade Group crossfade in the order they appear on the Channels screen. Negative CVs crossfade toward channels lower on the screen (i.e., higher numbered channels). Positive CVs crossfade toward channels higher on the screen (i.e., lower numbered channels).

> NOTE: Members of a Crossfade Group do not have to be contiguous on the Channels screen. They could even be interspersed between members of another Crossfade Group. For example, the following would be perfectly functional, giving independent control of the three groups:

 1. Group A
 2. Group A
 3. Group B
 4. Group C
 5. Group A
 6. Group B
 7. Group C
 8. Group C

### DATA 2 Assignment

To select the CV input that the DATA 2 knob will replace when you are on the home screen (or turn it off), navigate to the D2CV field and make your selection. When DATA 2 is assigned to replace a CV input, any CVs appearing at the selected input are ignored.

# 10. Zones

The Zones function lets you assign up to 8 samples to each channel and select between them in real time via a CV.

zone with a selection range of -5V to +5V.  Otherwise it will become the bottom (highest numbered) zone.

On the Zones screen, you can select the sample for each zone, set the voltage ranges that select each zone, assign the CV input that controls zone selection, and specify if zone switching happens only on gate rise or instantly as soon as the controlling CV crosses a selection boundary.

To quickly experience zones, load the Demo- Zones folder on your SD card and play around.

Here’s how it all works:

### Creating Zones

To create zones, start by selecting the channel you want to set up with zones and pressing the Zones/Select button to display the Zones screen.

If the channel has already had a sample assigned to it, that sample will be displayed on the Zones screen as a single zone with a selection range of -5V to +5V, along with the “++” new zone selection field. If the channel has not had a sample assigned to it, you will only see the new zone selection field.

To add a zone, highlight the “++” field and click the encoder. The Select Sample window will appear. Scroll to the sample of your choice and click the encoder again to select it. If this is the first zone created, it will appear on the zone screen as a single

> NOTE: If the sample you assign has been used in another preset in your folder, it will already be present in memory, so will be immediately available to play. However, if the sample has not been used in another preset, the on-demand loader will automatically load it into memory from your SD card. If it’s a short sample, you probably won’t even notice the delay. But if it’s a long sample, you may have to wait for a bit. You can refer to the progress bar at the top of the display for load status.

### Importing Samples

You can also import a sample from another folder on the currently inserted SD card into a zone. See Chapter 6 for details on importing samples.

> NOTE: If you replace an existing zone sample with a different sample, the new sample will inherit all of the channel’s channel parameters, along with any existing zone- dependent parameters (Pitch, Level, Sample Start/End, and Loop Start End/Length) that had been set for the previous zone sample.  You may (or may not) need to adjust those as desired.

### Copying Zones

If you’ve previously programmed a zone (either in the current channel or in another channel in your preset) that you would like copy into a zone in the currently selected channel, highlight the destination zone’s sample (or the ++ field for a new zone) and long press the encoder switch.  This will bring up the Copy Zone field. Scroll to the zone that you’d like to copy into the selected zone and click the encoder.

> IMPORTANT NOTE: The sample assigned to Zone 1 will also appear in the sample name field for the selected channel on the Channels page. If you replace that sample on the Channels page, it will, as you might expect, replace the sample in Zone 1. If you delete that sample on the Channels page, it will indeed delete Zone 1. (See Deleting Zones below for details on how that affects the remaining zones.)

### Selecting Zones

When on the Zones screen, you can select a zone simply by highlighting its sample name.  You can also select a zone from any screen by pressing and holding the Zones/Select button and pressing the channel button whose number corresponds to the zone you want to select (e.g., to select Zone 4, press the Channel 4 button). While that’s not too useful while on the Zones screen (it’s typically easier to use the encoder), it comes in really handy when you’re editing the other zones- dependent parameters: Pitch, Level, Sample Start/End, and Loop Start End/Length. Using that technique, you can select various zones and edit them in sequence without having to leave the parameter screen.

### Voltage Selection Ranges

Each time you add a new zone, the default voltage selection range for that zone is half of what was the voltage range for the zone above it.

“Huh?” you might well be thinking. If so, let’s look at how the default ranges work:

With one zone, the default range is -5V to +5V (i.e., the entire voltage range).

When you add a second zone, the default ranges are now:
Zone 1: +5V to 0V
Zone 2: 0V to -5V

Now add a third zone and it becomes:
Zone 1: +5V to 0V
Zone 2: 0V to -2.5V
Zone 3: -2.5V to -5V

I.e, Zone 3 has split what was Zone 2’s range in half, leaving Zone 1 unaffected.

Add another and you get:
Zone 1: +5V to 0V
Zone 2: 0V to -2.5V
Zone 3: -2.5V to -3.75V
Zone 4: -3.75V to -5V

Now Zone 4 has split what was Zone 3’s range in half, leaving Zone 1 and Zone 2 unaffected.

This process continues until you’ve added all the zones you want.

At that point, you’ll probably want to adjust the various voltage ranges for your particular needs. There are two ways to do that:

#### Automatic Equalization

This one’s easy.  If you want all of the zones to have an equally sized voltage range, just highlight any voltage field (it doesn’t matter which one) and long-press the encoder. The ranges will be automatically adjusted to that each zone’s range is of equal size.

#### Manual Adjustment

You can also navigate to each voltage field and adjust it with the DATA 2 knob or the encoder. When adjusting a voltage, it can not be made greater than the value above it or less than the value below it, so you may need to make some iterative adjustments to get exactly what you want.

### Gate Rise vs Continuous Modes

As mentioned above, you can specify if zone switching happens only on a trigger or gate rise, or instantly as soon as the controlling CV crosses a selection boundary.

Here’s how that works:

#### Gate Rise Mode

In Gate Rise Mode, each time a channel receives a gate rise or trigger (or its channel button is pressed), the zone selection CV value is read and the zone associated with that value is triggered. Changes to the CV value between triggers have no effect.

#### Continuous Mode

In Continuous Mode, the zone selection CV value is continuously monitored and a new zone is selected as soon as the CV value indicates.

> NOTE: In Continuous Mode, the new zone starts at the time position corresponding to the point in the first zone where the switch happens. E.g., If 2 seconds into the Zone 1 sample you switch to the Zone 2 sample, the Zone 2 sample starts at its 2 second position.  This works best if all samples are the same length or the channel is set to latch (i.e. repeat continuously).

If you switch to a new zone that has passed its end point (because it’s shorter than the zone it’s transitioning from and is not set to loop), playback will stop.

## Deleting Zones

To delete an existing zone, highlight the zone’s sample name, click the encoder to bring up the Select Sample window and rotate the encoder counterclockwise until “- -“ is displayed. Click the encoder. The zone will be deleted, the higher numbered zones will move up fill in the blank spot, and the deleted zone’s voltage range will be added to the range of the next higher numbered zone.  All zones above the deleted zone (i.e., lower numbered zones) are unaffected.

Again, an example might be helpful:

Before deletion:
Zone 1: +5.0V to 0V
Zone 2: 0V to -2.5V
Zone 3: -2.5V to -3.75V
Zone 4: -3.75V to -4.37V
Zone 5: -4.37V to -5.0V

After deleting the original Zone 3:
Zone 1: +5.0V to 0V
Zone 2: 0V to -2.5V
Zone 3: -2.5V to -4.37V
Zone 4: -4.37V to -5.0V

i.e., The original Zones 4 and 5 have now moved up to be the new Zones 3 and 4. The new Zone 3 has annexed the old Zone 3’s range of -2.5V to -3.75V, leaving Zones 1, 2, and 4 (the previous Zone 5) unaffected.

# 11. Play Mode/Latch

The Play Mode/Latch button lets you select the way in which a channel responds to a trigger or gate.

> NOTE: In addition to its associated LEDs, Play Mode status is also displayed on the Envelope screen and can be set from there as well.

Press the Play Mode button to cycle through its settings. The choices are:

### 1 Shot Mode

In 1 Shot Mode, a trigger or rising edge of a gate initiates the playing of a channel’s sample. Once initiated, the sample will play to its end (if its loop has been turned off) and stop, or, if its loop is turned on, will continue in that loop until manually stopped by pressing and holding the Play Mode button and then pressing the channel button.

1 Shot Mode is ideal for drum or other percussive sounds where you want to start a sample at the appropriate time and then simply have it play through to its end.

### Gated Mode

In Gated Mode, the rising edge of a gate initiates the playing of a channel’s sample.  Once initiated, the sample will play as long as the gate is high (or until it gets to its end, if its loop is turned off). When the gate falls, the sample will decay at the rate set by the Release parameter in the Envelope screen.

In regular Loop Mode (when the top Loop Mode LED is lit), upon gate fall, the sample remains in its loop while it decays.

In Gated Loop Mode (when the bottom Loop Mode LED is lit), upon gate fall, the sample will progress to its end (without any subsequent looping) while its decays.

### Latch Mode

Pressing and holding the Play Mode button and then pressing a channel button puts that channel into Latch Mode. Latch Mode is the equivalent of pressing and holding the channel button (without having to physically hold it — Latch Mode is holding it for you).  The LED of a channel in Latch Mode will flash to indicate its status. The channel will remain in Latch mode until the channel button is pressed again, at which time it will decay at the rate set by the Release parameter in the Envelope screen.

Latch Mode affects channels as follows:

  1. Latch Mode holds a channel’s gate high, so additional triggers or gates arriving at the channel’s Gate/Trigger input will not cause a re-attack.
  2. For a channel in Gate Mode, Latch Mode is exactly the equivalent of pressing and holding that channel’s channel button
  2. For a channel in 1 Shot Mode, Latch Mode differs in that when you press the channel button a second time to exit Latch Mode, it will also decay at the rate set by the Release parameter in the Envelope screen (which would not normally happen in 1 Shot Mode).

> NOTE: If a channel is using zones, the Play Mode setting affects all of the samples in the various zones.

# 12. Envelope

The Envelope lets you define the Attack and Release times for a channel’s or zone’s sample.

A sample or zone always attacks for the Attack time set here. A sample in Gated Mode (or in 1-Shot Mode using Latch Mode) decays for the Release time set here.

### Attack Time

Attack Time sets the time, in seconds, it takes from the moment a gate or trigger is received for the sample to reach its full programmed level. The range is from instantaneous to 99.00 seconds.

The resolution is as follows:

From 0.0000 (instantaneous) to 0.0099 seconds, the resolution is 1 ten thousandth of a second.

From 0.010 to 0.099 seconds, the resolution is 1 thousandth of a second.

From 0.100 to 0.990 seconds, the resolution is 1 hundredth of a second.

From 1.00 to 9.90 seconds, the resolution is 1 tenth of a second.

At 10 seconds and above, the resolution is 1 second.

The Attack Time can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter.

### Attack Start Value

This setting allows you specify the envelope’s starting voltage when its channel receives a trigger or gate. Its primary use is to decide what happens when a channel is playing and gets a new trigger before its envelope has come to its end.

The choices are:

#### From Zero Volts

As the name implies, this causes the envelope to always start at zero volts.

#### From Last Voltage

This setting causes the envelope to start at whatever its voltage is at the instant it receives a new trigger.

> NOTE: If sounds on a channel are not triggered such that they overlap, this setting has no effect, as the envelopes will always start from zero. However, if the sounds do overlap, depending on the sample and where it’s retriggered, “From Last Voltage” can sometimes eliminate clicks or other artifacts that result from large instantaneous voltage transitions. On the other hand, there are some situations, again depending on the sample and where it’s retriggered, where you’re going to get a click no matter what. But see the next note:

> ANOTHER NOTE: Another way to further minimize clicks on re-triggering is to turn on Smoothing in the Mutate screen. See Chapter 18 for details.

### Release Time

Release Time sets the time, in seconds, it takes from the moment a gate fall is received for the sample level to reach zero. The range is from instantaneous to 99.00 seconds.

The resolution is the same as for Attack Time above.

The Release Time can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter.

### Play

This field reports the Play Mode as set by the Play Mode button. The Play Mode can also be set here, in which case the Play Mode button’s LEDs will change in response.

### Loop

This field reports the Loop Mode as set by the Loop Mode button. The Loop Mode can also be set here, in which case the Loop Mode button’s LEDs will change in response.

### Trigger On Select

This setting allows you to specify what happens to this channel when its preset is initially selected. The primary focus of the parameter is for live performances where you’d want to load a preset and have one or more channels automatically start playing.  It is also useful for channels used as LFOs or other repeating CVs.

The choices are:

#### Normal

What you’d normally (hence its name) expect. Noting happens until the channel receives a gate or trigger, at which point it starts playing.

#### Auto

The channel will start playing automatically as soon as the preset is selected.

> IMPORTANT NOTE: In Auto Mode, a trigger is automatically sent to the channel when the preset is selected. So channels in Auto Mode should usually be set to 1-Shot (with or without a loop, depending on your intent).  If they’re set to Gated, they will be getting what is essentially an instantaneous gate and, depending on the setting of their envelope, may not sound at all.

> NOTE: If a channel is using zones, the Envelope settings affect all of the samples in the various zones.

# 13. Loop Mode

The Loop Mode button lets you turn a channel’s loop on and off as well as select the loop’s behavior during the envelope’s Release phase.

> NOTE: In addition to its associated LEDs, Loop Mode status is also displayed on the Envelope screen and can be set from there as well.

Press the Loop Mode button to cycle through its settings. The choices are:

### Loop Off

When neither of the Loop Mode button’s LEDs are lit, the selected channel’s loop is tuned off.

### Normal Mode

When the top LED is lit, the loop is in Normal Mode. In this mode, upon gate fall, the sample remains in its loop while it decays.

### Gated Mode

When the bottom LED is lit, the loop is in Gated Mode. In this mode, upon gate fall, the sample will progress to its end from wherever it is (without any subsequent looping) while its decays.

> NOTE: If a channel is using zones, the Loop Mode setting affects all of the samples in the various zones.

# 14. Loop Start and End/Length

This screen lets you define a loop within your sample which, depending on the Play Mode and Loop Mode settings, will cause a portion of the sample to repeat. The loop can be as short at 4 samples or as long as the entire length of the sample file.

## About the Display

In addition to the numerical positions (in samples) of the Start Point and the End Point or Loop Length, the screen also includes a graphical waveform display of the entire sample, as well as a high resolution display of the region around the point being adjusted designed to help you find the best loop points. The high resolution display provides individual sample resolution.

In the overview display, the start point marker is green and the end point marker is red. In the high resolution display, the red center line represents the splice point between the loop end point and the loop start point.

If the channel has been reversed, the waveform display shows a red border to remind you of that fact.

When adjusting either point, use the DATA 2 knob to get in the general neighborhood of where you’d like it to be. If you then highlight the appropriate numerical field and click the encoder to bring up the editing field, you can adjust the point in single sample increments.

> NOTE: You can bring up the screen by pressing either the Loop Start or Loop End/ Length buttons. The screen will appear with the selected numerical field highlighted. Once the screen is displayed, you can use the two buttons to switch back and forth between the two points for editing. (You can, of course, also use the encoder to navigate to either field.) If you press either button twice in succession, you will dismiss the screen.

## How Loops Work

A loop is a section of your sample that (unless it is turned off by the Loop Mode setting) will repeat under circumstances defined by a channel’s Play Mode and Loop Mode settings.

Here’s how:

#### Loop Off

When both Loop Mode LEDs are off, the loop is turned off.

#### Gated Play Mode + Normal Loop Mode (top LED lit)

The sample will start playing in response to a gate rise and will continue playing, with the loop repeating, as long as the gate is high. When the gate falls, the sample will remain in the loop while it decays at the rate set by the Release parameter in the Envelope screen.

#### Gated Play Mode + Gated Loop Mode (bottom LED lit)

The sample will start playing in response to a gate rise and will continue playing, with the loop repeating, as long as the gate is high. When the gate falls, the sample will progress to its end (without any subsequent looping) while it decays at the rate set by the Release parameter in the Envelope screen.

#### 1 Shot Mode Play Mode + Normal or Gated Loop Mode

The sample will start playing in response to a trigger or gate rise and will continue playing, with the loop repeating, until manually stopped by pressing and holding the Play Mode button and pressing the Channel button in question.

## Loop End vs. Loop Length

All loops, by definition, have a start and end point. But there are two ways to specify the end point: End Point or Loop Length.

Here’s how they differ:

#### End Point

When you specify an end point, you are specifying a specific independent location in the sample. It will only change if you manually move it or modulate the position with a CV or the DATA 2 knob (if that’s what it’s programmed for). Moving the Start Point, for example, will have no effect on it.

When you are in End Point mode, the numerical display on the loop screen will show the location of the end point in samples.

You will typically chose End Point mode when you want to ensure that a sample loops at a specific point in the sample.

#### Loop Length

In Loop Length mode, you specify the length of the loop relative to the Start Point. In Loop Length mode, the length is always fixed. Consequently when you move the start point, either manually or by modulating the position with a CV or the DATA 2 knob, the end point will also move to maintain the programmed length.

When you are in Loop Length mode, the numerical display on the loop screen will show the length of the loop in samples.

You will typically chose Loop Length mode when the loop is matched to a rhythm or tempo and you want to ensure that the loop is always exactly the same length.

### Selecting the Mode

To select the desired mode, make sure the End or Length field is highlighted and then press and hold the Loop End/Length button to toggle to the alternate mode. You will see the chosen mode (LEN or END) in the screen title and the modulation field’s title.

## Using the High Resolution Display

If you are programming a sample to loop while its audio is playing (as opposed to just looping a rhythmic phrase at its beginning and end), you will typically want to program the smoothest loop splice possible. While the Smoothing function described in Chapter 18 can help with that, it will do a much better job if you’ve programmed the best possible loop to begin with. That’s what the high resolution display is designed to help with.

As mentioned above, the red line at the center of the display represents the splice point between the loop’s end point and its start point. Although it may initially seem a bit counter-intuitive, the left side of the display is the region of the end of the loop, leading up to the end point as defined by the red line.  The right side of the display is the beginning of the loop, with the start point defined by the red line. (Trust us. It makes sense if you think about it.)

The goal in programming a good loop is to end up with the smoothest transition across the red splice point. There are two main elements to a smooth loop: a smooth level transition at the splice point and a smooth shape transition.

To get a good level transition, choose points such that the samples at either side of the red splice point are as close to the same value as possible. Level discontinuities typically result in clicks at the loop points.

To set a good shape transition, try to find points where the samples on either side of the red spice point are moving in roughly the same direction at roughly the same slope.

While it’s not always possible to find points that perfectly satisfy both of those goals, the closer you can get to them, the better the loop.

In both cases, use the DATA 2 knob to get close to the region where you want your loop, and then use the encoder to adjust the points in single sample resolution to get the best result.

## Loop Start

Loop Start sets the point that the loop loops back to when the loop end point is encountered. The position of the start point can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter. Positive CVs move the start point towards the end of the sample, while negative CVs move it toward the beginning of the sample. Modulation gain can be set over a range of from -1.00 to +1.00.

> NOTE: You can never move the start beyond the current position of the end point, either manually or via modulation.  The shortest loop allowed by Assimil8or is 4 samples, so if you move or modulate the start point as close to the end point as allowed, you will end up with a loop 4 samples in length.

> ANOTHER NOTE: In Loop Length mode, you will not be able to move or modulate the start point any closer to the end point than the programmed loop length. Once movement of the start point causes the end point to reach the end of the sample, you will be unable to move the start point any further in that direction.

> YET ANOTHER NOTE: The default loop points for a new sample are at the beginning and end of the sample. If you are in Loop Length mode, you will be unable to move the start point at all until you have moved the end point to define a new, shorter, loop length, or changed from LEN to END mode.

## Loop End

Whether it’s defined as an absolute location or by length, the Loop End Point sets the point at which the sample loops back to the loop start point. The position of the end point or the loop length (depending on mode) can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter. Positive CVs move the point towards the end of the sample, while negative CVs move it toward the beginning of the sample. Modulation gain can be set over a range of from -1.00 to +1.00.

> NOTE: You can never move the end point before the current position of the start point, either manually or via modulation.  The shortest loop allowed by Assimil8or is 4 samples, so if you move or modulate the end point as close to the start point as allowed, you will end up with a loop 4 samples in length.

> ANOTHER NOTE: In Loop Length mode, you will not be able to move or modulate the end point any closer to the start point than the programmed loop length. Once movement of the end point causes the start point to reach the beginning of the sample, you will be unable to move the end point any further in that direction.

## Smoothing

The Smoothing function described in Chapter 18 can help smooth out the sound of a less than perfect loop splice. It’s actual effect will depend on the audio in question and how good the splice is to begin with.  Simply try turning it on and off and see if it makes a positive difference.

## Zones

If a channel is using the Zones function, the loop points can be set independently for each sample in a zone. Simply select each zone and adjust its settings.

The number of the currently selected zone is displayed in the upper righthand corner of the screen, along with the number of the currently playing zone (in red). It is possible for these to be different, so if you’re setting a zone’s loop points and don’t hear any effect, make sure the zone you’re hearing is the one you’re actually editing.

# 15. Pitch

The Pitch screen lets you set a channel’s initial pitch, set a zone pitch offset if the channel contains zones, and set up exponential and/ or linear pitch modulation.

## Pitch

Pitch lets you set the initial pitch of the channel over a range of from 8 octaves below to 5 octaves above the originally sampled pitch with a resolution of 0.01 semitone.

> NOTE: If you click the encoder to bring up the full resolution editing field, pressing the encoder switch while turning the encoder will quantize the pitch setting to even semitones.

The Pitch can be exponentially modulated by any of the CV inputs with the modulation gain set by the associated attenuverter.  Modulation gain can be set from -2.00 octaves per volt to +2.00 octaves per volt.

> NOTE: For the typical 1 octave per volt modulation response, the pitch mod attenuverter should be set for a modulation gain of 0.50 (which is its default value).

## Zone Offset

If the selected channel contains zones, you can select each zone in the channel and apply a pitch offset to that zone. The range is from 8 octaves below to 5 octaves above the channel’s initial pitch as set by the Pitch parameter above.

> NOTE: The number of the selected zone is displayed in the upper righthand corner of the screen, along with the number of the currently playing zone (in red). It is possible for these to be different, so if you’re making changes to the zone offset and don’t hear any effect, make sure the zone you’re hearing is the one you’re actually editing.

> ANOTHER NOTE: The total upward transposition range of a 48kHz sample is limited to a +6 octave range. If, for example, the Channel pitch parameter is set to +4 octaves, the zone offset can only shift it an additional two octaves higher. Setting the zone offset higher than that will have no additional effect. The upper limits for other sample rates are: 24kHz=+7 octaves, 96kHz=+5 octaves, 192kHz=+4 octaves.

## Linear Frequency Modulation

Lets you assign the CV source and modulation gain for linear frequency modulation.  Modulation gain can be set from -200% per volt to +200% per volt.

## Exponential Frequency Modulation

Lets you assign the CV source and modulation gain for a second exponential frequency modulation. Modulation gain can be set from -2.00 octaves per volt to +2.00 octaves per volt.

# 16. Level

The Level screen lets you set a channel’s initial level, set a zone level offset if the channel contains zones, and set up exponential and/or linear amplitude modulation.

## Level

Level lets you set the initial level of the channel over a range of from -90.0 dB to +6.0 dB with a resolution of 0.1 dB.

## Zone Offset

If the selected channel contains zones, you can select each zone in the channel and apply a level offset to that zone. The range is from -90.0 dB to +6.0 dB relative to the channel’s initial level as set by the Level parameter above.

> NOTE: The number of the selected zone is displayed in the upper righthand corner of the screen, along with the number of the currently playing zone (in red). It is possible for these to be different, so if you’re making changes to the zone offset and don’t hear any effect, make sure the zone you’re hearing is the one you’re actually editing.

> ANOTHER NOTE: The total level adjustment range of any sample is limited to the -90.0 dB to +6.0 dB range. If, for example, the Channel Level parameter is set to +4.00 dBs, the zone offset can only shift it an additional 2 dBs higher. Setting the zone offset higher than that will have no additional effect.

## Linear Amplitude Modulation

Lets you assign the CV source and modulation gain for linear amplitude modulation. Modulation gain can be set from -20% per volt to +20% per volt.

## Linear Amplitude Modulation Bias

Linear Amplitude Modulation Bias lets you bias the level such that amplitude can be correctly controlled by an external envelope patched to the assigned modulation CV input. Specifically, you want zero volts from that envelope to result in no output level (rather than no modulation).

The choices are:

- Normal  No bias. Zero volts of CV results in no modulation.
- External Envelope The level is biased down such that zero volts of CV results in no audible output and higher CV levels introduce audibility (i.e., an envelope does what you’d expect an envelope to do).

## Exponential Amplitude Modulation

Lets you assign the CV source and modulation gain for exponential amplitude modulation. Modulation gain can be set from -1.200 dBs per volt to +1.200 dBs per volt.

# 17. Phase Modulation

Here’s where all the phase modulation magic happens.

If you’re not already familiar with phase modulation, please check out Dave’s Intro to Phase Modulation in Chapter 25.  Then check out the Demo- PhaseMod folder on your SD card (read a description of it in Chapter 22). Then come back here. We’ll wait.
…
…
…

Back? Great.

There are two parts to setting up phase modulation on a channel: Selecting the modulator and specifying the modulation index.

### Phase Modulation Source

The modulation source can come from any of Assimil8or’s channels (including the channel you’re programming), from either the right or left sampling input, or from any of the 24 CV inputs.

To select the modulator, highlight the source field and click the encoder or use DATA 2 knob to select the source. If you select a channel or sampling input, you’re done.

If instead, you select “Select CV,” the CV field, along with its associated attenuverter (which are otherwise grayed out) will turn white to indicate they are active. Highlight the CV select field to select your desired CV. Use the attenuverter to set the CV Gain in a range of from -1.00X to +1.00X at a resolution of 0.01.

> NOTE: Even when a CV is not selected as the Modulation Source, you can still navigate to the grayed out CV and CV Gain files and adjust them. However, they have no effect until “Select CV” is selected in the Modulation Source field.

### Phase Modulation Index

The Modulation Index sets the intensity of the modulation source’s effect. It ranges from 0.00 to 1.00 at a resolution of 0.01. This corresponds to a range of from 0.0 to 256.0 samples.

The Modulation Index can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter.  Modulation gain can be set from -51.2 samples per volt to +51.2 samples per volt.

> A TIP: Phase modulation as implemented in Assimil8or is in some ways a new territory to explore. Certainly as far as samples modulating samples is concerned. We strongly encourage experimentation in the choice of both modulators and carriers. Experiment with pitch intervals between the modulators and carriers. Experiment with individually modulating the pitches of the modulators and carriers. Go crazy.

# 18. Mutate

The Mutate screen includes a number of parameters that allow you to subtly (in the case of Smooth) or not so subtly (in the case of everything else) modify your sounds.

## Bit Depth

This parameter lets you hear your sample as it would sound if it were stored at bit depths of from 32.0 bits down to 1.0 bit. Resolution is 1 bit from 10.0 to 32.0 bits and 0.1 bit from 1.0 to 10.0 bits. (That’s right, you can finally hear what a 5.3 bit format would sound like.)

> NOTE: Playing with this parameter will demonstrate that the difference between high and medium bit depths are really quite subtle. If you really want to destroy your sounds, start around 6 bits or so and head down from there.

> ANOTHER NOTE: It’s a good idea to turn down the volume before exploring the lowest bit depths. As you get down to 1 bit, you’ll get to the point where your sound is just a full-level square wave. A LOUD full-level square wave. Be careful.

Bit Depth can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter. The gain range is from -3.20 bits per volt to +3.20 bits per volt.

## Aliasing

Dave has developed some really amazing pitch shifting technology to allow Assimil8or to transpose sounds up and down over a huge range without artifacts. The Aliasing control lets you progressively disable that technology so that you can introduce those aliasing and imaging artifacts into your sounds (if that’s the sort of thing you’re into).

> IMPORTANT NOTE: Aliasing only results when a sampled sound is pitch shifted.  Therefore, this parameter will only have an effect on a sound that’s being pitch shifted, allowing the artifacts that are normally eliminated by Dave’s technology to become audible. The more it’s pitch shifted, the greater the potential effect.

However, if you’re just playing back a sample at its original pitch (or not pitch shifting very far), the Aliasing parameter will have no effect at all, as there will be no artifacts generated in any case.

Here’s what the various settings of Aliasing do:

#### From 0% to 25% aliasing

only the aliasing while pitch shifting upward will be affected. What is happening is that we are reducing the degree to which we track the alias reduction filter to the pitch. Higher pitch shifts get more and more aliasing over this range. Beginning at 25%, the pitch will no longer affect the interpolator filter at all.

#### From 25% to 36%

we gradually reduce the steepness of the anti-aliasing filter, gradually allowing more aliases.  Somewhere around 31% the quality will be that of the G-chip, as used in all E-mu samplers since Proteus, Emax II, and E3X.  At 36%, the quality is similar to what was used in the EMU8000 chip that powered the Sound Blaster AWE32.

#### From 36% to 51%

The interpolator transitions from a brick-wall lowpass filter to (at 51%) a linear interpolator.

#### From 51% to 89%

The interpolator transitions from a linear interpolator to (at 89%) a drop sample interpolator. Linear interpolation is used by most sample playback engines; drop sample was used by instruments from the PPG, through the Ensoniq Mirage, to the SP1200.

#### Beyond 89%

the “extreme alias” regime is entered. The interpolation filter no longer remains lowpass, and aliases are emphasized. At 100%, the filter has a highpass characteristic, so the aliases are louder than the fundamental sound.

Aliasing can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter. The gain range is from -100% per volt to +100% per volt.

## Reverse

Turning Reverse on, as you might expect, causes the selected channel to play in reverse. Here’s what happens when a channel is playing in reverse:

- The sample data, including start and end points and loop points are reversed. On the Start/End and Loop screens, you will see the wave data and associated markers in their reversed orientation. You will also see the waveform displays outlined in red to remind you that things are reversed.
- Playback begins at what was the sample’s programmed end point (which is now the start point) and proceeds towards what was the sample’s programmed start point (which is now the end point).

- Loops begin at what was the sample’s programmed loop end point (which is now the start point) and proceeds towards what was the sample’s programmed loop start point (which is now the end point).

- Positive modulation of both Sample Start and End and Loop Start and End/Length push the appropriate markers towards the end of the reversed sounds (i.e., what was its beginning before reversal).

- If you reverse a sound that is playing, the Smoothing function described below is applied to the splice to help minimize (but probably not eliminate) any clicks or other artifacts.

## Smoothing

This function enables a proprietary splicing algorithm to points where otherwise noncontiguous audio data is joined in an attempt to minimize clicks or other artifacts.

The following points only have smoothing applied when this parameter is set to “On”:

**Loop Points**
**Sample re-triggering** (i.e., restarting a sample from its beginning before it has completed playing)
**Gated zone switching** re-triggering (i.e., triggering a new zone sample before the previous zone sample has completed playing)

> NOTE: Smoothing can be more or less effective depending on the specific audio involved (and your design intent). For any particular splice, just try turning it on and off and decide what works best.

The following points always have smoothing applied:

**Realtime zone switching**
**Reversing** while a sample is playing

# 19. Shuttle and Scrub

## Shuttle and Scrub

Rather than being dedicated functions, shuttling and scrubbing are accomplished by the appropriate programming of existing Assimil8or parameters. To understand how to accomplish each, refer to the instructions below.

> NOTE: If you’re impatient to try them, load the folder “Demo-Scrub&Shuttle” from your SD card. The presets are described in Chapter 22. You can also use these presets as templates for your own sounds. Simply copy one or more of them to a new folder and replace the template samples with ones of your own.

### Shuttling

Shuttling is the process of controlling the speed and direction of playback of a channel by a CV (or the DATA 2 knob assigned to a CV — which is a good way to get the feel for it).

To set up a channel for Shuttling:

1. Assign the sample you want to Shuttle to a channel.
2. In the Pitch screen, set the pitch to -60.00 semitones.
3. Also in the Pitch screen, assign a CV input to Linear FM.
4. Set the Linear FM Gain to 1.00. The CV assigned to Linear FM will now control shuttling.
6. Go to the main home page (so DATA 2 is active) and latch your channel on.
7. Turn the DATA 2 knob as desired.

Here’s how it works:

- When the CV is positive, the sample plays forward. The greater the CV value, the faster the sample plays.
- When the CV is negative, the sample plays backward. The greater the negative CV value, the faster the sample plays backward.
- When the CV is 0 Volts, the sample stops playing altogether at the point where the CV became 0.
- If no loop is set and the sample plays forward to its end, the sample will stop and need to be re-triggered to play again.
- If a loop is set, the sample will continue to play forward as long as a gate is present (if Gated) or indefinitely (if 1 Shot)
- If you play the sample backwards towards its beginning, it will stop playing when its Start Point is reached. However, if the CV is then moved to a positive value, the sample will start playing forward again from the Start Point.

> A TIP: Given the extraordinary quality of Dave’s pitch shifting technology, some amazing sounds and textures can be found at values just slightly above or below 0 volts. Try it!

### Scrubbing

Scrubbing is the process of directly controlling the playback position and speed of a sample. Scrubbing is controlled either by a CV or the DATA 2 knob assigned to a CV — which, again, is a good way to get the feel of it.

To set up a channel for Scrubbing with the DATA 2 knob:

 1. Assign the sample you want to Scrub to a channel.
 2. In the Pitch screen, set the sample’s pitch to +60.00 semitones
 3. In the Loop screen, create a 4 sample loop in Start/Length mode at the approximate center of the sound.
 4. Assign a CV to modulate the loop start with a gain of 0.71
 5. Assign the DATA 2 knob to the CV selected in Step 4.
 6. Go to the main home page (so DATA 2 is active) and latch your channel on.
 7. Turn the DATA 2 knob as desired.

# 20. Pan/Mix

The Pan/Mix screen lets you assign a channel (or not) to the Mix Outputs, set the channel’s level and initial pan position, and set up CV control of pan.

## Pan

Pan lets you set a channel’s initial position in the stereo field. The range is from -1.00 (full left) to +1.00 (full right). In addition to the numerical indication, there is a graphical display of position.

The pan position can be modulated by any of the CV inputs with the modulation gain set by the associated attenuverter. Modulation gain can be set from -40.0% per volt to +40.0% per volt.

## Mix Output Level

Mix Output Level lets you set a channel’s level in the Mix Outputs independent of its level at its Individual Output. The range is from -89.9 dB to +6.0 dB with a resolution of 0.1 dB.

Additionally, at the far counterclockwise end of the control range is a setting of “Off,” which completely removes the channel from the Mix Outputs.

# 21. Utilities

The Utilities menu is where you’ll find Assimil8or’s various housekeeping and maintenance functions.

To access the Utilities menu, press the Utilities button. Turn the encoder to scroll through the available function list.  Click the encoder to choose the desired function.

The menu is dismissed by pressing the Utilities button again.

Here are the available Utility functions:

## Memory Usage

The Memory Usage screen gives you both numerical and graphic indications of how much of your available memory is used by the currently loaded folder (including any new samples you’ve made since loading the folder).

## SD Card Usage

The SD Card Usage screen gives you both numerical and graphic indications of how much of the available storage space on the currently inserted SD card is used by saved data. If no card is present in the front panel slot, the screen will display “Card Not Ready.” If that happens, put a card in the slot (as if you need us to tell you that).

## OLED Control

As mentioned back in Chapter 5, OLED displays have long lifetimes under normal use, but if you leave your system on 24/7 (or just want to ensure the longest possible life for your display), you can adjust the brightness of the display (which is also useful for optimizing it for the ambient lighting level of your work environment) and, optionally, you can set a time after which the display enters a screensaver mode. Both of these can help extend the life of your display.

> NOTE: Once the screen saver has appeared, any button press or a turn of the encoder will dismiss it and return to the regular display. Such encoder turns or button presses are not registered as control inputs.

> ANOTHER NOTE: The screen saver will not appear when you are executing a Utilities Menu function. However, it will appear if the Utilities Menu is displayed (but no function selected).

Here’s how it works:

1. Select Utilities > OLED Control on your Assimil8or.
2. Turn the encoder to select a brightness level of 1-11. You’ll see the display change in brightness as you scroll through the values. The value number also changes color to indicate their effect on OLED life (Green=great, Yellow=okay, Red=beware if you leave your system on 24/7)
3. Click the encoder to move to the ScreenSaver setting.
4. Turn the encoder to select the time after which the screen saver will appear.  Choices range from 2 minutes to 60 minutes and “Never.” If you consistently leave your system on long periods of time, “Never” is probably not a good choice.

## New Folder

Unsurprisingly, the New Folder function allows you to create a new empty folder on the currently inserted SD card. Clicking on this function initially brings up the Name New Folder field, which is preloaded with default name (in a code that has been lost to all but a few intrepid programmers) that you are almost certainly going to want to change.

Change the name using the technique described in Chapter 6. Then press and hold the encoder for 2 seconds to save your new folder to your SD card.

> NOTE: When renaming a new folder, be sure that you give it a unique name. If you give it a name that is already used on the current SD card, you will receive the error message “File Exists” and the folder will not be created.

> ANOTHER NOTE: Creating a new folder does not automatically load it. After creating it, your most currently loaded folder will still be in memory. You will need to use the Load function to access the new folder.

## Folder Utilities

This function offers a variety of utilities for managing folders.

Press the Folder Utilities button to bring up a list of folders on the currently inserted SD card. Select the folder you wish to modify and click the encoder to bring up the Folder Utilities window. Select your desired action and click the encoder to proceed.

The options are:

#### Rename

Allows you to rename the folder.  Change the name using the technique described in Chapter 6.

> NOTE: You can not change the name of the currently loaded folder.

#### Duplicate

Allows you to create a copy of the selected folder on the inserted SD card and to rename the copy. Change the name using the technique described in Chapter 6 and then press and hold the encoder for 2 seconds to save the copied folder to your SD card.

> NOTE: You must change the name of the folder before saving or you will get the message “File Exists” and the copied folder will not be saved.

#### Delete

Allows you to delete the selected folder. Upon clicking Delete, you will be asked if you are sure (as the deletion is permanent). If you are sure, click “Delete” to complete the deletion.

> NOTE: You can not delete the currently loaded folder.

## Load Software

This function lets you load updated operating software into your Assimil8or. The process is very straightforward, but it does require that you have the ability to download a file from the internet and copy it onto a micro SD card.

 1. From the Downloads tab of the Assimil8or web page (<www.rossum-electro.com/> products/ assimil8or/), download the zip archive containing the latest Assimil8or software. Unzip the archive to find the software file entitled “app.”
 2. Copy the app file to the root level of your micro SD card and insert the card into the front panel slot on you Assimil8or.
 3. Select Utilities > Load Software and click the encoder.
 4. Assuming you inserted your SD card in
Step 2, click the encoder as instructed.
 5. If all goes well (which it almost certainly will), you will see a success message and instructions to turn the encoder and then click it to reboot your Assimil8or with the new software.
 6. If an error is detected during the process, an error message will be displayed and you can try again.
 7. Enjoy your new software.

## Load Boot Software

This function loads an updated version of the special software that’s responsible for booting up your Assimil8or.  It’s pretty unlikely you’ll ever have to do this, but if you do, the process is pretty much identical to the Load Software function above, with the exception that you will be downloading and loading a file entitled “MLO.”

## Format SD Card

This function formats a micro SD card to be used in Assimil8or. The process erases anything that was previously on the card, so if you’re formatting a card that has anything on it, make sure that none of that anything is something you want to keep.

To format the card, insert the card to be formatted and click the encoder. You’ll get an appropriately dire waring. To proceed, turn the encoder and click again. A progress bar with indicate the progress of formatting. If all goes well, you’ll get a success message.

After formatting, the card will contain an empty folder called “bank”. You can use it, rename it, or delete it as desired.

## Make Boot Card

Assimil8or includes a second micro SD card inserted in the processor board on the rear of the module. This card includes Assimil8or’s operating software, along with the software required for Assimil8or to boot up. Under most circumstances, you should never need to access or interact with this card. However, if you ever want or need (for whatever reason) to have a backup boot card, this function will allow you to create one.

The process is exactly like the Format SD Card process described above. After formatting, the card will contain an “app” file (the operating software) and an “MLO” file (the boot software).

> NOTE: The app and MLO files created in this process are the ones present on the boot card installed in your Assimil8or. If, for some reason, you end up installing this card in the future, if there’s been an intervening software update, you should update the software using the Load Software function described above.

## Calibrate

Your Assimil8or is carefully calibrated at the factory. So, under normal circumstances, you shouldn’t have a need to recalibrate it. However should abnormal circumstances present themselves, this function allows you to recalibrate your Assimil8or.

Before attempting to calibrate your Assimil8or, please carefully read Dave’s calibration instructions in Chapter 23.

If you decide to proceed, select Utilities > Calibrate on your Assimil8or and follow the instructions on each screen.

At the end of the process, you will be able to choose whether you want to save your new calibration. Press the encoder to save it, or press UTILITY to exit without saving the calibration.

## Manufacturing Test

This function provides a suite of tests to be used during manufacturing to ensure that everything on your Assimil8or is working correctly. Unless something goes horribly wrong, there shouldn’t be a reason that you ever need to worry about it.

However, like Calibrate, it’s self-guiding, so if you’re just curious, you’re welcome to play with it, since it can’t do any harm.

## About this Module

Selecting this function displays your Assimil8or’s current version of installed software. You can always find the latest software version on the Assimil8or web page. You’ll want to check here to see if you’ve got that latest version.

# 22. Sample Sounds and Demos

To help get you started, some of our talented beta testers have been kind enough to provide some of their samples and presets for your use. See the descriptions below.

We’ve also provided some presets designed to demonstrate some of Assimil8or’s unique capabilities. They can, if you like, be used as templates for your own presets using those features. To use them as templates, load the one you want and then immediately resave it to a different location and rename it. (That way the original template is still available unchanged for when you want to use it again.) Then just replace the demo samples with your own and adjust the channel parameters as desired.

IMPORTANT NOTE: You are free to use the provided samples and presets in your own music and audio projects (including projects for sale). However, you may not resell or otherwise distribute the samples and/or presets nor use them in any other product.

## Demo Folders

### Demo-Cycle

The Demo-Cycle folder contains two presets that demonstrate the Cycle function. In both presets, press the Channel 1 button repeatedly or patch a repeating trigger into Channel 1’s Gate/Trig input.

**Preset 001**: A synthesized voice speaking a number sequentially on each channel.
**Preset 002**: A series of metallic percussive sounds that’s indicative of one of the typical ways Cycle could be used to provide a variety of related sounds that overlap naturally on repeated triggers.

### Demo-Link

The Demo-Link folder contains contains a single preset with 6 channels linked to provide a dense layered texture. Press the Channel 1 button or patch a trigger into Channel 1’s Gate/Trig input to trigger all 6 channels simultaneously.

### Demo-PhaseMod

The Demo-PhaseMod folder contains three presets that use then same set of 8 channels.  Each pair of channels are configured such that the odd numbered channel is the carrier and the even numbered channel is the modulator.  Each pair of channels is linked, so you only need to trigger the odd numbered channel of each pair

**Preset 001**: The DATA 2 knob controls the pitch of the carrier.
**Preset 002**: CV A of the carrier’s channel (the odd numbered one) controls the pitch of the carrier.
**Preset 003**: CV A of the carrier’s channel controls the pitch of the carrier. And DATA 2 controls the Modulation Index.

**Preset 002**: A demo of Zones in Continuous mode. Press and hold the Channel 1 button (or send a long gate into Channel 1’s Gate/ Trig input) and turn the DATA 2 knob. You will hear the zone switch immediately every time the control CV passes a selection boundary.  Turn the knob really fast for some interesting effects.

Sample Sounds and Presets
Jim Aikin
Some audio craziness from composer and technology writer (and, it might also benoted, fantasy author) Jim Aikin.

Aikin Grunge: One preset with 8 demented channels of samples taken directly from the Microbe 3qu4tion Composer. All channels have CV A patched to Pitch.

Brad Bowden
Producer and sound designer Brad Bowden assembled an extensive collection of classic and modern electronic percussion units to create a library of pristine sampled drum kits.

SubID Drums: 30 meticulously configured drum kits based on original samples of a pantheon of electronic drum machines. All channels have CV A assigned to Pitch.

According to Brad, instruments sampled include: E-mu SP1200, TR 808, TR 909, TR 606, Elektron Machinedrum, Elektron RYTM, Elektron Monomachine, Circuit Bent Yamaha DD7, Circuit Bent Alesis HR-16, Noise Engineering Basimilus Iteritas Alter, and Yamaha CS80.

Recording gear included: Audio Sonic Lens, Retro Instruments Powerstrip, Vintech X81, Empirical Labs Distressor, Mytek 8ch ADDA, Neve Master Bus Processor, Dangerous Music Bax EQ, Burl Mothership, Universal Audio DSP, and PL Transient Designer.

### Demo-Scrub&Shuttle

The Demo-Scrub&Shuttle folder contains templates for programming shuttling and scrubbing.

**Preset 001**: A sample of dialog (to let you know where you are in the sample). Press the Channel 1 button and use the DATA 2 knob to shuttle forward and backward at various speeds as described in Chapter 19. As mentioned there, some amazing sounds and textures can be found at values just slightly above or below 0 volts. Try it!
**Preset 002**: The sample dialog sample. This time DATA 2 scrubs through the sample.
**Preset 003**: The same as Preset 001, except here, CV1B controls the shuttling.

### Demo-XFade

The Demo-XFade folder contains two presets based on the same 8 linked channels programmed to be in the same crossfade group. Press the Channel 1 button or patch a trigger into Channel 1’s Gate/Trig input to trigger them.

Preset 001: The DATA 2 knob controls a crossfade of all 8 channels. With a width of 3.8V, there is quite a bit of overlap in the resulting audio.
Preset 002: The same as Preset 001, except here the crossfade is controlled by CV1A.

### Demo-Zones

The Demo-Zones folder uses Channel 1 set up with 8 zones, each of which is a synthesized voice speaking a number sequentially on each zone (i.e., Zone 1 is “one,” Zone 2 is “two,” etc.).

Preset 001: A demo of Zones in Gate Rise mode. While turning the DATA 2 knob, press the Channel 1 button repeatedly or patch a repeating trigger into Channel 1’s Gate/Trig input. Each time the button is pressed or a trigger is received, you will hear the zone sample corresponding to the CV value at that moment.

Richard Devine
A varied selection of loops and single-shot samples from composer and sound designer Richard Devine.

As a bonus (and not, as far as we can tell, having anything to do with clicks), there’s an additional preset of motor relay and revving sounds.

All of Richards’s samples are in 44.1khz, 24-bit wave format. They have all been normalized and mastered to -0.1 for volume and consistent playback. All channels have CV A patched to Pitch, CV B patched as Phase Mod source, and CV C patched to Phase Mod Index

Devine Loops: 30 stereo loops distributed over 8 presets, all at 120BPM. In this collection, Richard created some fun abstract beat loops, textures, and textured sequences.  He encourages you to go crazy with the CV inputs via pitch control, scrubbing, and phase mod etc.

Devine SingleShots: 40 stereo single shot sounds distributed over 8 presets. Richard created these entirely with synthesis from the ground up. They include some fun musical one-shots, that include chord stabs, pads, bass notes, arp/bell/SFX/hits,and a variety of different percussion sounds.

## Reek Havok

An eclectic collection of electronic percussion and occasional craziness from percussionist, programmer, sound designer, and interactive consultant, Reek Havok.

Havok 8Bit: One preset with 8 channels of crunchy 8-bit fun (or, as Reek refers to it, “phun”).
Havok 808 Drums: Two full kits of 808 drum samples.
Havok Claps: 20 samples of various claps in 4 presets. Most of the samples are from Reek’s vintage 1980’s Simmons Clap Trap.
Havok Clicks: Three presets of various clicks in thee presets. Reek assures us that clicks are super popular right now. I guess we’ll have too trust him on that.

Havok KLANG: Three presets of heavy metal clangs and bangs.
Havok LFOs + CV: Demonstrating Assimil8or’s ability to sample CVs as well as audio, this folder contains 5 banks of sampled LFOs, as well as some crazy random voltages from Reek’s Frap Sapel.
Havok Numbers: Four presets of robotically spoken numbers. Great if you happen to need robotically spoken numbers. Try resampling the output of these presets while playing the different numbers and then experiment with modulation of sample start and end points and loop points of the resulting sample. Because of the counting, you’ll always know exactly where you are in the sample as you modulate things.
Havok Simmons Drums: 11 presets of kicks and snares sampled from Reek’s Vintage Simmons SDSV analog drum brain.
According to Reek, it’s the same one he used on many records, including the triple platinum “Breakout” album by the Pointer Sisters. (Neutron Dance, I’m so Excited, Automatic)

### Kurt Kurasaki

A tasty selection of synthesized drum kits from composer and sound designer Kurt Kurasaki, better known in some internet circles as Peff.

Peff Drums: 22 presets of synthesized drum kits. In each channel, CV A = Pitch (or FM), CV B is varied, but usually pan, AM, or bit depth, and CV C is Phase Mod Index

According to Kurt, these sounds were created on a number of different synths, including his Buchla and a variety of eurorack modules.  They were recorded through a DI and some nice mic-pres (Neve/REDD.47).

### Ben “DivKid” Wilson

A varied selection of drone and percussive samples from producer, composer, and famed video creator, Ben “DivKid” Wilson.

Ben has recorded these sounds as stereo samples with the left channel containing the dry sound and the right channel containing the same sound, but with various effects. Use them separately or together as you desire.

All channels have CV A patched to Pitch, CV B patched as Phase Mod source, and CV C patched to Phase Mod Index

DivKid Drones: 12 stereo (but see above) sample in 3 presets. A variety of single note drones that let you use Assimil8or like an oscillator, as well as chordal textures and a wider polyphonic ambient piece to play with.  DivKid Drums: 45 stereo (but again, see above) percussive samples in 13 presets. Ben synthesized some custom drum sounds, as well as recording some from a variety of modular drum units.

# 23. Calibration

Your Assimil8or module comes pre- calibrated from the factory. You should only recalibrate it for specific reasons.

If your system is already consistently calibrated to a 1V/octave standard, it might be that the factory calibration does not exactly match your system. In this case, you can calibrate your Assimil8or to the precision voltage standard you use for your system.  Alternatively, you can use Assimil8or’s precise factory calibration to tune the other sources in your system.

If for some reason your Assimil8or has specific calibration issues, such as a single inaccurate CV channel, or an input or output with non-zero DC offset, you can also calibrate individual inputs and outputs.

The Assimil8or also allows you to check the calibration of its 24 CV inputs and the offset of its sample inputs.

In all cases, please read these instructions completely before beginning calibration.

Adjusting the output and sample input voltage offsets (but not 1V/octave sensitivity) is very easy and requires nothing special.

If you want to calibrate your Assimil8or to your local 1V/octave (what we are really doing is making your Assiml8or and the rest of your system agree as to what is considered one Volt), you will need an accurate source of both +4.000V and -4.000V. A Rossum Electro-Music Control Forge module is ideal for this purpose, but any source that can accurately output +4.000V and -4.000V will do. You may need to use a precision inverter to get -4.000V if you only have a +4.000V precision source. Make sure your voltage source has essentially zero ohms output impedance!

critical note: if you do not have a way to apply precisely +4.000v and -4.000v to the assimil8or, don’t try to re-calibrate the cv inputs.

eurorack systems vary greatly in the quality of their grounding. check assimil8or’s ground by adding patch cords between unused inputs across modules while you are checking your calibration. If the voltage changes significantly as you add patch cords, your system’s grounding is at fault. There may not be too much you can do about it, but using a short power cable to Assimil8or is particularly important. If you have questionable grounding, and want to take advantage of the Assiml8or’s CV accuracy, be sure to use good, thick patch cords, and use them to connect as many grounds as you can between Assimil8or and the sources of your precision CVs. Patching unused inputs between CV source and destination modules is a good way to add grounds.

To begin calibration, press UTILITY, scroll down to “Calibrate,” and press the encoder.  Press the encoder again when you are ready to proceed. (Note that at any point you can exit calibration by pressing the UTILITY button, and until you’ve chosen to save your new calibration, nothing will be changed.)

At this point, you can check the calibration of your Assimil8or.  To check a CV channel, apply a known voltage, and rotate the encoder to select the input you are using.  Assimil8or’s CV

inputs should be accurate to 2-3mV over a -5V to +5V range.

The next screen shows only the input CVs you are calibrating, probably in red.  Apply exactly -4.000V to the CVs you are calibrating; they should turn green. Once you’ve done this, press the encoder to proceed.

The next screen shows you all the CV inputs that will NOT be re-calibrated in red. From here you can rotate the encoder CCW and go back to calibrate more CV inputs, or press the encoder to accept your CV calibrations and proceed to calibrate the output offsets.

The next screen requests that you patch each Channel output to its corresponding CV A input, and patch the Mix Outputs to the Sample Inputs. Each channel number (or letters L or R) will go from red to green when the corresponding patch cord is detected.  Once you’ve done this and all the characters are green, press the encoder to proceed.

The next screen will tell you if any of the patch cords were not inserted or if any output could not be calibrated. Press the encoder to proceed.

You now can choose if you want to save your new calibration. Press the encoder to save it, or press UTILITY to exit without saving the calibration.

By the way, if you don’t own a voltmeter and need one for calibrating one of the other modules in your system, you can use this feature of your Assimil8or to do this! If you want to calibrate your keyboard (or other voltage source) to the Assimil8or, use this mode and adjust the source module to produce what Assimil8or says is exactly 1V/ octave. (It’s best to calibrate with the highest voltage available, for example if you have a 4 octave keyboard, adjust the lowest key to 0.000V and the highest to 4.000V). It’s best to use Assimil8or’s CV A inputs in this mode; they are slightly more accurate than the CV B and CV C inputs.

Assimil8or’s sample inputs should have an offset (what is displayed when 0V is applied or nothing is plugged in) within 1-2mV of zero, and be accurate to about 1% of any applied voltage (4.000V should read between about 3.960V and 4.040V).

(Because Assimil8or’s signal path has a 1.00k Ohm output impedance, the gain will vary about 1% depending on the input impedance of its load, so we don’t calibrate the signal path gain.)

Once you’re done checking your calibration, press the encoder to proceed to the next step.

You can calibrate inputs individually or in any combination.

The next screen shows all the input channels, probably in green. If you are calibrating one or more particular CV inputs to a 1V/octave source, you should connect that source to those inputs and set it to output 0.000V.  Leave the sample input jacks and any CVs you don’t plan to calibrate open. Once you’ve done this, press the encoder to proceed.

The next screen again shows all the input CVs, probably in red. Apply exactly +4.000V from your precision source to any CVs you are calibrating; they should turn green.

Once you’ve done this, press the encoder to proceed.

# 24. Specifications

CHANNELS
8

SAMPLE RATES
48kHZ, 96kHZ, 192kHZ

A/D AND D/A
24 Bits

INTERNAL PROCESSING
32 Bits

OUTPUTS
MIX L/R
2x 3.5mm mono socket
1kΩ Impedance

INDIVIDUAL OUTPUT 1-8
8x 3.5mm mono socket
1kΩ Impedance

POWER REQUIREMENTS
+/-12V (+/- 5%) via 16-pin, Doepfer-style
connector

LATENCY
100 microseconds at the Mix Outputs, 180
microseconds at the Individual Outputs

CURRENT DRAW
220mA +12V, 30mA -12V

SAMPLE MEMORY
2300 seconds (mono at 48kHz) freely
allocatable between channels

DIMENSIONS
28 HP (W); Panel to power connector (with
connector plugged in) 25mm (D)

SUPPLIED ACCESSORIES
1x Micro SD card
1x 16-pin, Doepfer-style cable
4x M3 screws
4x M2.5 screws
4x Nylon washers
1x Quickstart Guide

PRESETS
Up to 199 per Folder

INPUTS
SAMPLE L/R
2x 3.5mm mono socket
100kΩ Input Impedance

GATE/TRIGGER 1-8
8x 3.5mm mono socket
100kΩ Input Impedance
1.6V threshold

CONTROL VOLTAGE A
8x 3.5mm mono socket
100kΩ Input Impedance
96 kHz sample rate
Anti-alias filtered to 20kHz bandwidth

CONTROL VOLTAGE B&C
16x 3.5mm mono socket
100kΩ Input Impedance
48 kHz sample rate
No anti-alias filtering

# 25. From Dave’s Lab

Intro to Phase Modulation

Let’s look at some oscilloscope photos to understand the difference. If I frequency modulate a sine wave with another sine wave, the ‘scope shows us the effect on the waveform. (The modulator is on the bottom in blue, the carrier in yellow on the top):

Now let’s use a pulse waveform to modulate a sawtooth wave carrier:

Phase modulation is a new kind of audio cross-modulation for sampled sounds. It can produce rich and varied timbres and textures, as well as wild distortions and grating noises.

The word “new” is probably not accurate.  Modular synthesizers have used frequency modulation (FM) since their inception. Low frequency FM produces nice vibrato effects, and audio rate FM creates interesting timbres.  But exponential FM alters the perceived fundamental frequency of an oscillator; linear FM is required to alter the timbre while staying on pitch.

When we use FM, we call the source of the modulation the modulator, and the oscillator being modulated is called the carrier.

In the early 1970’s, John Chowning discovered using digital oscillators that linear FM through the zero point (so the carrier actually reversed its oscillation) produced very diverse and pleasing timbres.  Yamaha further developed this technology, but while Yamaha continued to call their implementation “FM”, they actually were using Phase Modulation. Also worthy of note, Don Buchla heard Chowning say that you couldn’t do “through zero” FM with an analog circuit, so Don did just that with his Music Easel’s Complex Oscillator.

Here you can see that when the pulse is high, the sawtooth gets steep, when it’s low, the sawtooth slope is slight.

Now let’s use “through zero” modulation and turn up the gain of the modulator to show how the sawtooth slope now goes downward (backward) when the FM goes negative:

Here’s what a sawtooth phase modulated by a pulse looks like. When the pulse goes high, the carrier skips ahead to a higher point in the sawtooth ramp; when it goes low, it skips back to a lower point.

Now, a big problem with through zero linear FM is that as the pitch of the modulator goes up, it has less effect on the carrier’s timbre.  Here’s the same setup as above, but with the frequency of the modulating pulse wave increased by 1.5 octaves. Note that the carrier waveform is getting to be pretty much an ordinary sawtooth.

But now when we increase the modulator’s frequency, the carrier is still dramatically affected. And we can see also in this waveform cases where the pulse has skipped backwards or forwards over the sawtooth’s edge, creating more large edges at this point.

The solution, as Yamaha discovered, was to instead of modulating the carrier’s frequency, have the modulating oscillator modulate its “phase.” What this means is that the modulator is directly changing the location in the carrier’s waveform, rather than changing the rate that the carrier oscillates by moving along through its waveform.

We can modulate the sawtooth with a sine wave too. Here, you can see how phase modulation maintains the character of each waveform, giving a new timbre with the characteristics of both the modulator and the unmodulated carrier:

As a final example, here’s the waveform that results when a sawtooth is modulated by a violin sample. The frequency and sharp edges of the sawtooth are maintained, but the complex timbre of the violin is added:

When first planning Assimil8or, I thought phase modulation might be a neat feature.  I was really surprised to find almost nobody had taken advantage of phase modulated sampled sounds. My first few experiments were really exciting, and I hope you have fun exploring this capability of Assimil8or.

# 26. From Dave’s Lab: Circuit Protection

Eurorack suffers from the problem of power connector reversal. When 10 pin connectors are used, mis-insertion results in a swap of +12V and -12 V, and protection is easily accomplished using various techniques such as series diodes.

But more systems are providing the +5V supply and thus use the full 16 pin connector.  When this is reversed, a diode-protected module is still safe, but the six connected ground pins in the module will short together the system’s +5V and +12V supplies, potentially damaging the power supply and any modules that use +5V.

To prevent this, Rossum Electro-Music modules deviate from the standard Eurorack power connector by leaving power connector pins 9 and 10 open, rather than connecting them to ground. When plugged in backwards, this leaves the system +12V supply disconnected. Since ground is still supplied by four pins as well the chassis and any patch cords connected to the module, the dropping of these two pins has no measurable effect on circuit performance, but it means that if a Rossum Electro module is accidentally plugged in backwards, no stress is placed on the +5V supply or modules that use it.

# 27. Acknowledgements

The Assimil8or Cast and Crew
CONCEPT, USER INTERFACE
Dave Rossum
Bob Bliss
Marco Alpert

HARDWARE DESIGN
Dave Rossum

SOFTWARE DESIGN
Dave Rossum
Bob Bliss

MANUAL
Marco Alpert
Nancy Enge

PACKAGING, PANEL GRAPHICS
Nancy Enge

A number of wonderful people generously provided help, advice, encouragement, and inspiration during the development of Assimil8or.

Many thanks from the Rossum Electro-Music
team to:

Jim Aikin
Alex Anderson
Patrick Aurelio
Brad Bowden
Josh Cliffe
Richard Devine
András Eichstaedt
Nancy Enge
Reek Havok
Mihai Ionescu
Kurt Kurasaki
Mason Malvinni
William Mathewson
David Phipps
Bill Putnam Jr.
Kirk Southwell
Matt Tanner
Tyler Thompson
Ben “DivKid” Wilson

And, it goes without saying (but, as we always do, we’ll say it anyway), our families for understanding all the late nights and weekends spent not having fun (or doing chores) with them.
