import pandas as pd

def create_df(lists):
    """create data frame with relevant formatting"""
    df = pd.DataFrame(lists)
    return(df)

def create_sheet(df, imagename, colouring='std'):
    """create spreadsheet with given pixel values"""
    
    # with ... as ... should close the sheet automatically when done
    with pd.ExcelWriter(imagename+'-output-image.xlsx') as writer:
        df.to_excel(writer, header=False, index=False) # create spreadsheet

        worksheet = writer.sheets['Sheet1'] # set up worksheet

        (max_row, max_col) = df.shape
        # set up conditional formatting
        for row in range(max_row):
            # rows are zero indexed here
            if row % 3 == 0:
                colours = ['#000000','#800000','#FF0000'] # red
            elif row % 3 == 1:
                colours = ['#000000','#008000','#00FF00'] # green
            elif row % 3 == 2:
                colours = ['#000000','#000080','#0000FF'] # blue
            
            if colouring == 'invert':
                colours = colours[::-1]
            elif colouring == 'bws':
                colours = ['#000000','#808080','#FFFFFF']
            
            # cells should behave as pixels, colour intensity depending on numerical value in each cell
            worksheet.conditional_format(row,0,row,max_col, {'type': '3_color_scale',
                        'min_type': 'num', 'min_value': 0,
                        'mid_type': 'num', 'mid_value': 128,
                        'max_type': 'num', 'max_value': 255,
                                    'min_color': colours[0],
                                    'mid_color':colours[1],
                                    'max_color':colours[2]})