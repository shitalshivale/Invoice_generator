import streamlit as st
from invoice_generator import read_excel_data,generate_invoice

def main():
    upload_file = st.file_uploader("Upload excel file", type=["xlsx"])

    if upload_file is not None:
        sale_data= read_excel_data(upload_file)

        if sale_data is None:
            print(f"File is empty:{upload_file}")
        else:
            invoice_file_for_download= generate_invoice(sale_data)

            for pdf_file in invoice_file_for_download:
                with open(pdf_file, 'rb') as file:
                    st.download_button(
                        label=f"Download {pdf_file}",
                        data=file,
                        file_name=pdf_file,
                        mime="application/octet-stream"
                    )

# Entry point of the script
if __name__ == "__main__":
    main()
