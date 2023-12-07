# AutoSeqBuilder

## Introduction

AutoSeqBuilder is a Python script designed to simplify the automatic creation of video sequences with a resolution of 1800x1680 in your favorite editing software. The main goal of the script is to generate an XML file that can be easily imported into editing software such as Adobe Premiere Pro, DaVinci Resolve, and others.

## Key Features

- **Video Sequence Automation:** Automatically generates video sequences with a resolution of 1920x1080.
  
- **XML File Ready for Import:** Creates a structured XML file ready to be imported into your editing software.

## How It Works

The script takes an input file containing the paths to video files, each with a specific order, and generates a structured XML file. This XML file can be directly imported into your preferred editing software, respecting the specified order in the input file.

## Example Usage

Suppose you have an input file named "file_paths.txt" with the following video paths:

```plaintext
file '/percorso/del/file/file_video.mp4' 
file '/percorso/del/file/file_video2.mp4' 
file '/percorso/del/file/file_video3.mp4' 
```

Use AutoSeqBuilder as follows:

```bash
python AutoSeqBuilder.py file_paths.txt output
```

This will generate an XML file named "output.xml" that respects the specified order in your input file. You can then easily import this XML file into your preferred editing software to create a structured video sequence according to your needs.

## Importing into Editing Software

Once the XML file is created, import it by following the specific steps of the editing software you are using. For example, in Adobe Premiere Pro, select "File" > "Import" > "File" and choose your XML file. This will simplify the sequence creation process, saving you time and ensuring that the sequence structure exactly reflects your requirements.

With AutoSeqBuilder, automate the creation of your video sequences and streamline your editing workflow.
