def spreadsheet_encode_col(col_str):
    num =0
    count = len(col_str) -1
    for i in col_str:
        num += 26**count * (ord(i)-ord('A')+1)
        count -=1
    return num


print(spreadsheet_encode_col("AA"))
        