<!-- @format -->

# Label-Encoding

Label Encoding class is to label encode the data on required columns of you choice

## Usage

To use the code, you can just copy it as a code block or you can put the .py file in main directory of python packages.

## Example

```
# "df", "df_test" are respectively the train and test dataframe you are using, "target_col" is the column to predict.
# Note that these are used as example. None of them are defined here for simplicity.

from LabelEncoding import Label_Encoding

le = Label_Encoding(custom_encoding="partial", random_state=42) # custom_encoding can be True, False, "partial". False by default.
le.fit(df, df.columns, {target_col: {'A': 1.0, 'B': 2.0}})
le.transform(df)
le.transform(df_test)
```

### Feel free to modify it as your need, also contribute here!!!
