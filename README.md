# EnDuRLM

## Functionality

### Real world applications
- Next word generator for radiology language.
- Solve data leaks, bad quality or incoherence by replacing the missing word/sequence.
- Quality check to increase the accuracy of radiology reports.
- At the educational level, residents and students could benefit from a system that suggests specific terms and highlights wrong expression.

### Example of generated text using the most accurate model for each language

#### MIMIC:
- Screening analog mammography with icad computer aided detection the breasts are predominantly fatty.
- There is a N cm opacity seen in the upper outer quadrant.
- There are vascular calcifications however a single bb likely represents a small lymph node in the right retroareolar region.
- No evidence of malignancy. Birads N benign findings.

#### ZGT:
- Goed beoordeelbaar dens klierweefsel rechts mamma compositiebeeld b bij densiteit geen pathologische laesies of stellate laesies.
- Ter nadele van het tijdsinterval gebied leeg denser als rondom ieder N en drainage aanvullend.
- Echografie net boven van de areola thans een massa zichtbaar met littekenweefsel van N cm.
- Dientengevolge bevindingen op de mlo opname subcutis lateraal craniaal in de rechtermamma scherp densiteit gezien met niet positie.
- Birads N geen linker uit geesteren voelt sinds N maand knobbeltje in de borst n lateraal.

## Prerequisites
Code is organized in subfolders for data preprocessing, model training and model evaluation.

- Python 3
- PyTorch 0.4
- Juptyer Notebook

### Code execution steps
1. Run Juptyer Notebook data/data_preparation.ipynb and save output data.
2. Then with that data, run data/data_preprocess.ipynb.
3. (optional) In order to count data size, you can run data/data_countwords.ipynb.
4. To train the model and get generated text, run run.py. (This will call main.py and randomize parameters, in order to find best configuration)
5. Run get_log_data.py to generate a csv with the results.

## Models
Models used:
- [**LSTM**](https://arxiv.org/abs/1808.03314)
- [**AWD LSTM**](https://github.com/salesforce/awd-lstm-lm)
- [**FRAGE LSTM**](https://github.com/ChengyueGongR/Frequency-Agnostic)

## Data
Datasets used:
- [**MIMIC**](https://mimic.physionet.org/)
- [**ZGT Radiology Reports**](https://www.zgt.nl/)

Datasets were used under confidentiality agreements and therefore code doesn't contain any data.

## Paper
This repo contains code used for paper [**'Effectiveness of neural language models for word prediction of textual mammography reports'**](https://essay.utwente.nl/78779/) from *University of Twente*, which will be presented at [SMC2020](http://smc2020.org/).

### Abstract:
Radiologists are required to write free paper text reports for breast screenings in order to assign cancer diagnoses in a later step. The current procedure requires considerable time and needs efficiency. In this paper, to streamline the writing process and keep up with the specific vocabulary, a word prediction tool using neural language models was developed. Consequently, challenges as different languages (English, Dutch), small data sizes and low computational power have been overcome by introducing a novel English-Dutch Radiology Language Modelling process. After defining model architectures, the process involves data preparation, bilevel hyperparameters optimization, configuration transfer and evaluation. The model is able to improve the current workflow and successfully meet the computational constraints, based on both an intrinsic and extrinsic evaluation. Given its flexibility, the model opens the door for future research involving other languages and also an extensive set of real-world applications.

### Citation:
Bibtex format:
```
@misc{essay78779,
           title = {Effectiveness of neural language models for word prediction of textual mammography reports},
           month = {July},
          author = {Mihai David {Marin}},
            year = {2019},
        keywords = {ARRAY(0x561babb6b538)},
             url = {http://essay.utwente.nl/78779/}
}
```

## Acknowledgments
A big portion of code was retrieved and modified from https://github.com/salesforce/awd-lstm-lm.
