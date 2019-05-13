import json

python_object = {
  "input_fastq_read1_files": [ { "class": "File", "path": "/data/scratch/rna-seq/RNASeq_Dec2018/" } ],
  "input_fastq_read2_files": [ { "class": "File", "path": "/data/scratch/rna-seq/RNASeq_Dec2018/" } ],
  
  "default_adapters_file": { "class": "File", "path": "/opt/software/external/ggr-cwl/GGR-cwl-v1.0.0/v1.0/default_adapters_fromfastqc_30aug2018.fa" },
  "trimmomatic_java_opts": "-Xms1000m -Xmx1000m",
  "trimmomatic_jar_path": "/opt/software/external/trimmomatic/trimmomatic/trimmomatic-0.36.jar",
  "genome_sizes_file": { "class": "File", "path": "/data/transformed/STAR-2.6.1b/ensembl-93/danio_rerio-genome/chrNameLength.txt" },
  "sjdbOverhang": "100",
  "annotation_file": {"class": "File", "path": "/data/scratch/ensembl-93/danio_rerio-gtf/Danio_rerio.GRCz11.93.gtf"},
  "genome_fasta_files": [
    {"class": "File", "path": "/data/scratch/ensembl-93/danio_rerio-genome/danio_rerio.genome.fa"}
  ],
  "STARgenomeDir": {
      "class": "Directory",
      "location": "/data/transformed/STAR-2.6.1b/ensembl-93/danio_rerio-genome/"
  },
  "rsem_reference_files": {
      "class": "Directory",
      "location": "/data/transformed/RSEM-v1.3.0/ensembl-93/danio_rerio-genome/"
  },
  "bamtools_reverse_filter_file": {"class": "File", "path": "/opt/software/external/ggr-cwl/GGR-cwl/v1.0/quant/reverse_filter.duke_sequencing_core.txt"},
  "bamtools_forward_filter_file": {"class": "File", "path": "/opt/software/external/ggr-cwl/GGR-cwl/v1.0/quant/forward_filter.duke_sequencing_core.txt"},

  "nthreads_qc": 8,
  "nthreads_trimm": 8,
  "nthreads_map": 8,
  "nthreads_quant": 8
}

json_string = json.dumps(python_object)

new_python_object = json.loads(json_string)

