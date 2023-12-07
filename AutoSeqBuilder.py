##### AutoSeqBuilder
# -*- coding: utf-8 -*-

import os
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

def crea_xml_AutoSeqBuilder(input_file,nome_xml):
    # Creazione dell'elemento root <xmeml>
    root = Element("xmeml", version="4")

    # Aggiunta del doctype
    doctype = Comment("DOCTYPE xmeml")
    root.append(doctype)

    # Creazione dell'elemento <sequence>
    sequence = SubElement(root, "sequence")

    # Aggiunta dell'elemento <duration> sotto <sequence>
    duration = SubElement(sequence, "duration")
    duration.text = "67500"                  #67500 frame sono 45 minuti

    # Creazione dell'elemento <rate> sotto <sequence>
    rate = SubElement(sequence, "rate")

    # Aggiunta dell'elemento <timebase> sotto <rate>
    timebase = SubElement(rate, "timebase")
    timebase.text = "25"

    # Aggiunta dell'elemento <ntsc> sotto <rate>
    ntsc = SubElement(rate, "ntsc")
    ntsc.text = "FALSE"

    # Aggiunta dell'elemento <name> sotto <sequence>
    name = SubElement(sequence, "name")
    name.text = nome_xml

    # Creazione dell'elemento <media> sotto <sequence>
    media = SubElement(sequence, "media")

    # Creazione dell'elemento <video> sotto <media>
    video = SubElement(media, "video")

    # Creazione dell'elemento <format> sotto <video>
    format = SubElement(video, "format")

    # Creazione dell'elemento <samplecharacteristics> sotto <format>
    samplecharacteristics = SubElement(format, "samplecharacteristics")

    # Aggiunta dell'elemento <rate> sotto <samplecharacteristics>
    rate = SubElement(samplecharacteristics, "rate")

    # Aggiunta dell'elemento <timebase> sotto <rate>
    timebase = SubElement(rate, "timebase")
    timebase.text = "25"

    # Aggiunta dell'elemento <ntsc> sotto <rate>
    ntsc = SubElement(rate, "ntsc")
    ntsc.text = "FALSE"

    # Aggiunta dell'elemento <width> sotto <samplecharacteristics>
    width = SubElement(samplecharacteristics, "width")
    width.text = "1920"

    # Aggiunta dell'elemento <height> sotto <samplecharacteristics>
    height = SubElement(samplecharacteristics, "height")
    height.text = "1080"

    # Aggiunta dell'elemento <anamorphic> sotto <samplecharacteristics>
    anamorphic = SubElement(samplecharacteristics, "anamorphic")
    anamorphic.text = "FALSE"

    # Aggiunta dell'elemento <pixelaspectratio> sotto <samplecharacteristics>
    pixelaspectratio = SubElement(samplecharacteristics, "pixelaspectratio")
    pixelaspectratio.text = "square"

    # Aggiunta dell'elemento <fielddominance> sotto <samplecharacteristics>
    fielddominance = SubElement(samplecharacteristics, "fielddominance")
    fielddominance.text = "none"

    # Aggiunta dell'elemento <colordepth> sotto <samplecharacteristics>
    colordepth = SubElement(samplecharacteristics, "colordepth")
    colordepth.text = "24"

    # Creazione dell'elemento <track> sotto <video>
    track = SubElement(video, "track")

    # Leggi il file di testo contenente la lista dei nomi dei file video
    with open(input_file, "r") as file:
        video_files = file.read().splitlines()

    # Inizializza il contatore per start e end
    start_counter = 0
    end_counter = 250  # 250frame = 10sec

    # Creazione di un elemento <clipitem> per ciascun file video
    for video_file in video_files:
        if not video_file.strip():  # Verifica se la riga è vuota o contiene solo spazi vuoti
            
            continue  # Salta il resto del ciclo per questa riga vuota

        # Rimuovi spazi e caratteri di apertura/chiusura del file
        cleaned_string = video_file.strip().strip("file '").strip(" '")

        clipitem = SubElement(track, "clipitem")

        # Aggiunta dell'elemento <name> sotto <clipitem>
        name = SubElement(clipitem, "name")
        name.text = nome_file = os.path.basename(cleaned_string)

        # Aggiunta dell'elemento <enabled> sotto <clipitem>
        enabled = SubElement(clipitem, "enabled")
        enabled.text = "TRUE"

        # Aggiunta dell'elemento <duration> sotto <clipitem>
        duration = SubElement(clipitem, "duration")
        duration.text = "250"               # Specifica la durata della clip 10sec

        # Aggiunta dell'elemento <rate> sotto <clipitem>
        rate = SubElement(clipitem, "rate")

        # Aggiunta dell'elemento <timebase> sotto <rate>
        timebase = SubElement(rate, "timebase")
        timebase.text = "25"

        # Aggiunta dell'elemento <ntsc> sotto <rate>
        ntsc = SubElement(rate, "ntsc")
        ntsc.text = "FALSE"

        # Aggiunta dell'elemento <start> sotto <clipitem> posizione sulla timeline
        start = SubElement(clipitem, "start")
        start.text = str(start_counter)

        # Aggiunta dell'elemento <end> sotto <clipitem>
        end = SubElement(clipitem, "end")
        end.text = str(end_counter)

        # Aggiunta dell'elemento <in> sotto <clipitem>
        in_element = SubElement(clipitem, "in")
        in_element.text = "0"

        # Aggiunta dell'elemento <out> sotto <clipitem>
        out = SubElement(clipitem, "out")
        out.text = "250"

        # Aggiunta dell'elemento <alphatype> sotto <clipitem>
        alphatype = SubElement(clipitem, "alphatype")
        alphatype.text = "none"


        # Creazione dell'elemento <file> sotto <clipitem>
        file_element = SubElement(clipitem, "file", id=f"file-{cleaned_string}")

        # Aggiunta dell'elemento <name> sotto <file_element>
        file_name = SubElement(file_element, "name")
        file_name.text = cleaned_string

        # Aggiunta dell'elemento <pathurl> sotto <file_element>
        pathurl = SubElement(file_element, "pathurl")
        pathurl.text = f"file://{cleaned_string}"

        # Aggiunta dell'elemento <rate> sotto <file_element>
        rate_file = SubElement(file_element, "rate")

        # Aggiunta dell'elemento <timebase> sotto <rate_file>
        timebase_file = SubElement(rate_file, "timebase")
        timebase_file.text = "30"

        # Aggiunta dell'elemento <ntsc> sotto <rate_file>
        ntsc_file = SubElement(rate_file, "ntsc")
        ntsc_file.text = "TRUE"

        # Aggiunta dell'elemento <duration> sotto <file_element>
        duration_file = SubElement(file_element, "duration")
        duration_file.text = "250"

        # Creazione dell'elemento <media> sotto <file_element>
        media_element = SubElement(file_element, "media")

        # Creazione dell'elemento <video> sotto <media_element>
        video_element = SubElement(media_element, "video")

        # Creazione dell'elemento <samplecharacteristics> sotto <video_element>
        samplecharacteristics_element = SubElement(video_element, "samplecharacteristics")

        # Aggiunta dell'elemento <rate> sotto <samplecharacteristics_element>
        rate_sample = SubElement(samplecharacteristics_element, "rate")

        # Aggiunta dell'elemento <timebase> sotto <rate_sample>
        timebase_sample = SubElement(rate_sample, "timebase")
        timebase_sample.text = "25"

        # Aggiunta dell'elemento <ntsc> sotto <rate_sample>
        ntsc_sample = SubElement(rate_sample, "ntsc")
        ntsc_sample.text = "TRUE"

        # Aggiunta dell'elemento <width> sotto <samplecharacteristics_element>
        width_sample = SubElement(samplecharacteristics_element, "width")
        width_sample.text = "1800"

        # Aggiunta dell'elemento <height> sotto <samplecharacteristics_element>
        height_sample = SubElement(samplecharacteristics_element, "height")
        height_sample.text = "1680"

        # Aggiunta dell'elemento <anamorphic> sotto <samplecharacteristics_element>
        anamorphic_sample = SubElement(samplecharacteristics_element, "anamorphic")
        anamorphic_sample.text = "FALSE"

        # Aggiunta dell'elemento <pixelaspectratio> sotto <samplecharacteristics_element>
        pixelaspectratio_sample = SubElement(samplecharacteristics_element, "pixelaspectratio")
        pixelaspectratio_sample.text = "square"

        # Aggiunta dell'elemento <fielddominance> sotto <samplecharacteristics_element>
        fielddominance_sample = SubElement(samplecharacteristics_element, "fielddominance")
        fielddominance_sample.text = "none"
    
        start_counter+=250
        end_counter+=250

    nome_xml = str(nome_xml)  # Convert nome_xml to a string if it's not already
    filexml = nome_xml + ".xml"
    # Genera l'albero XML e scrivilo in un file
    tree = ElementTree(root)
    tree.write(filexml, encoding="UTF-8", xml_declaration=True)
    print("FILE XML creato con successo")


#da cancellare quando si importa come libreria - da usare come test
#input_file = "percorsi_file_trovati.txt"
#crea_xml_AutoSeqBuilder(input_file,"output")

