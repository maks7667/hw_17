"""
я не смог проверить код потому что я не могу создавать excel файл
"""
import pandas as pd

if __name__ == "__main__":
    df1 = pd.read_excel("1111.xlsx")
    df2 = pd.read_excel("2222.xlsx")
    df3 = pd.read_excel("3333.xlsx")

    combined_df = pd.concat([df1, df2, df3])

    sorted_df = combined_df.sort_values(by=list(combined_df.columns), ascending=False)

    with pd.ExcelWriter("combined_sorted.xlsx", engine="openpyxl") as writer:
        sorted_df.to_excel(writer, index=False, sheet_name="Sheet1")
        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]

        font = workbook.add_format({'bold': True})
        worksheet.set_row(0, None, font)
        for col in range(sorted_df.shape[1]):
            worksheet.set_column(col, col, None, font)

        border_format = workbook.add_format({'border': True})
        worksheet.conditional_format(0, 0, sorted_df.shape[0], sorted_df.shape[1],
                                     {'type': 'no_blanks', 'format': border_format})
    