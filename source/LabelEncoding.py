# Rquired packages
import random

class Label_Encoding:
    '''
        before encoding you need to set up which columns you want to label encode.
        Note that, ideally you will use fit function create the encoding.
        Otherwise if you want to use your custom made encoding you can do so.
        The process to custom encode is that you need to create a nested dictionary.
        The main dictonary will have keys as column names you want to encode, and as values,
        you need to use a dictonary which will have keys as category and value as encoded values.
        If you want to encode only train data, you can do with fit_tranform method.
        You can use the tranform method to encode the test data. It will autometically
        handle the categories which yet to encode.

        Example
        ["df", "df_test" are respectively the train and test dataframe you are using, "target_col" is the column to predict.
        Note that these are used as example. None of them are defined here for simplicity.]

        from LabelEncoding import Label_Encoding

        le = Label_Encoding(custom_encoding="partial", random_state=42) # custom_encoding can be True, False, "partial". False by default.
        le.fit(df, df.columns, {target_col: {'A': 1.0, 'B': 2.0}})
        le.transform(df)
        le.transform(df_test)
    '''
    def __init__(self, custom_encoding=False, random_state=None):
        self.custom_encoding = custom_encoding
        self.random_state = random_state
        # self.encoder = None
        self.d = None
        self.cols_to_encode = None
        self.extra_encode = {}
    
    # Creates dictionary of encodes.
    def _create_dict(self, df, columns):
        d = {}
        for col in columns:
            d_tmp = {}
            l = list(df[col].unique())
            if np.nan in l:
                l.remove(np.nan)
            x = list(range(1, len(l)+1))
            x = [float(f) for f in x]
            random.shuffle(x)
            for i in range(len(l)):
                d_tmp[l[i]] = x[i]
            d[col] = d_tmp
        return d
    
    # Fits the data
    def fit(self, df, columns, encoding_dict=None):
        self.cols_to_encode = columns
        if not self.custom_encoding:
            if self.random_state is not None:
                random.seed(self.random_state)
                self.d = self._create_dict(df, columns)
            else:
                self.d = self._create_dict(df, columns)
        elif self.custom_encoding == "partial":
            assert isinstance(encoding_dict, dict), "encoding_dict must be a dictionary"
            assert encoding_dict is not None, "If you want partial encoding you need to add at least something in encoding_dict"
            columns = list(set(columns).difference(set(encoding_dict.keys())))
            # print(columns)
            if self.random_state is not None:
                random.seed(self.random_state)
                # print(encoding_dict)
                encoding_dict.update(self._create_dict(df, columns))
                self.d = encoding_dict
            else:
                encoding_dict.update(self._create_dict(df, columns))
                self.d = encoding_dict
        else:
            self.d = encoding_dict
            assert self.d is not None, "Please enter the dictionary of encoder, otherwise you can change custom_encoding to False"
        return self.d
    
    def _transform(self, df, dct):
        for col in dct.keys():
            df[col] = df[col].map(dct[col])

    # Fits the data and then transforms it with label encode
    def fit_transform(self, df, columns, encoding_dict=None):
        self.cols_to_encode = columns
        enc_d = self.fit(df, columns, encoding_dict)
        self._transform(df, enc_d)

    # Transforms it with label encode
    def transform(self, df):
        enc_d = self.d
        self._transform(df, enc_d)
        for col in self.cols_to_encode:
            unq = [f for f in df[col].unique() if f is not np.nan]
            enc_ed = enc_d[col].values()
            re_coded = list(set(unq).difference(set(enc_ed)))
            # print(re_coded)
            if len(re_coded) > 0:
                re_dct = {}
                x = max(enc_ed) + 1
                for el in re_coded:
                    re_dct[el] = X
                    x += 1.0
                self.extra_encode[col] = re_dct
                df[col] = df[col].map(re_dct)
    
    # To check what variables got created during the process
    def info(self):
        print("Encoded dictonary: {}".format(self.d))
        print("Random state of this run: {}".format(self.random_state))
        print("Extra encoding on transformed data: {}".format(self.extra_encode))
        print("------End of Information-------")