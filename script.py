from pdf2image import convert_from_path
pages = convert_from_path(
    pdf_path='docs/Timothy_Wangwe_Resume_v2.pdf',
    output_folder="assets/img/pdf",
    output_file="Resume_v2",
    fmt="PNG",
    dpi=300,
)