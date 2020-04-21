# strehltools
tools for plotting AO simulation results

## Data Format Requirements
In order to use these tools at the most user-friendly level, you are required to save your simulation results in a very specific format. Hopefully, as we develop these tools, we will also include some copy-pastable functions to include in your YAO/COMPASS simulations to handle this formatting for you.

### Results `.fits` File
The `.fits` file containing the simulation results as well as metadata in the file header will be read by the `strehltools` library. This `.fits` file must have the following structure:

|  **Extension**   |    **Data**    |          **Shape**           |
|------------------|----------------|------------------------------|
|   0 (Primary)    |  `StrehlData`  | `[N_TARGET,5]`               |
|   1              |  `LEPSF`       | `[N_TARGET,IM_XDIM,IM_XDIM]` |
|   2              |  `PupilMask`   | `[IM_XDIM,IM_XDIM]`          |

#### `StrehlData`
The `StrehlData` is made up of 5 columns and `N_TARGETS` rows. Each row contains the following information:

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
|`xpos`|`ypos`|`lambda`|`ase`|`le`|

#### `LEPSF`
Long Exposure PSF image on a square support of size `[IM_XDIM,IM_XDIM]`; one for each target, stacked along the first dimension. 

#### `PupilMask`
Pupil mask of the telescope, in order to generate the ideal diffraction limited PSF etc.

### Metadata
The metadata contained in the header for the primary fits extension should contain the unique identifier (UID) for the simulation, which in principle can be used to compare simulation parameters and run-time log (assuming we set up some kind of archiving system).

## Types of plots to be built
- 2D Wide Field ASE/LE Heat Map (strehl/nm rms)
- 1D averaged radial performance plot (strehl/nm rms)
- 2D tip-tilt *ellipses* across FoV

## Usage
1) import the library,
```
import strehltools as st
```

2) load the results,
```
st_data = st.load("results.fits")
```

3) plot the plots,
```
st_data.heatmap(exposure="ase",units="strehl",xlim=[-15,15],ylim=[-15,15])
```
