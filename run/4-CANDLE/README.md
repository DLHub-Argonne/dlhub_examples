CANDLE and DLHub
----------------

This notebook demonstrates using DLHub to publish and use two CANDLE models: P1B1 and Combo.

Due to the size of the P1B1 model the p1b1.h5 file has not been included in this repository. Instead, needs to be trained using the P1B1 codes available here:

https://github.com/ECP-CANDLE/Benchmarks/tree/master/Pilot1/P1B1

We have included a subset of the training data here in the pilot1.npy file.

This repository also includes the Combo model as two files: a saved architecture and saved weights. The Combo model requires a custom layer. Our notebook shows how to both specify this custom layer's use and how to append the file into the metadata and thus publication of the model.

For information on how to either acquire an example p1b1.h5 file, or help training your own version please contact us.
