# Mirrur
**Hack RPI Fall 2019 x Project Mirror**
Assisted Journalling with NLP for Mental Health

Wolfram Award Winner 🎉

## Goal
Help pre-depressive/hopeless behaviors through customized supportive messaging and, if necessary, provide a report to share with health care professional to find inflection points.

With data coming from a text as an anonymous shared journalling platform, we collected natural language from users from text messages and responded with proper texts in accordance with their hopelessness index (0-1). At lower levels, we referred users to mental health specialists with an online anonymous report they could access. This report offered the ability to find changes in hopelessness over time.

**Presentation Link**
https://docs.google.com/presentation/d/1ld6yPPlV6nb9XL2jQKcTsk6SC9VIfFV61sRsD5DCPRI/edit#slide=id.p4

**NLP Heuristics (Averaged for hopelessness index)**
- Absolutism/Polarization Index (0-1 Index for usage of words like "always", "never", "completely")
- Global Sentiment (0-1 Positivity Word Values Summed and mapped to 0-1 score)
- Last Entry Sentiment (Same as Global Sentiment but just for latest entry to weight the present)

*Note: Polarization was found to be highly predictive of hopeless behavior, for this reason we made sure to focus our efforts on here. It was a challenge weighting the index based on the amount of these determiners, adjectives and adverbs relative to the total count of these parts of speech in the body of text*

## Tools & Technologies
- Python NLTK Package for Parts of Speech Tagging (Polarization Index)
- Google Cloud Platofrm Natural Language API (Sentiment Analysis)
- Twilio SMS API
- DigitalOcean (VM & Networking)
- .xyz domain (https://mirrur.xyz) [will most likely be down later]

## Pictures/Screenshots

*Example Journal*
![Example Journal](https://raw.githubusercontent.com/jshom/mirrur/master/images/demo-text.jpg)

*Example Full Report*
![Example Full Report](https://raw.githubusercontent.com/jshom/mirrur/master/images/demo-report.jpg)

## Contributors
- Brian Wu
- Andres Orbe
- Justin Kwong
- Jacob Shomstein
