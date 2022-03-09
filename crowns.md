# Standard output from LidR Crown Metrics 
## R LidR command is 
crown_metrics <- delineate_crowns(ctg_seg, func = .stdmetrics)
Where ctg_seg is a normalized point cloud with a unique treeID

| Variable Name | Description | References | Units | Type |
|---|---|---|---|---|
| fid |Feature Identifier – a unique identifier for the item |   |Dimensionless |Int64 |
| treeID |Tree Identifier – a unique ID for the tree |   |Dimensionless |float64 |
| XTOP |Maximum x value of all tree points |   |Projected Units |float64 |
| YTOP |Maximum y value of all tree points |   |Projected Units |float64 |
| ZTOP |Maximum z value of all tree points. Same as zmax |   |Projected Units |float64 |
| zmax |Maximum height |   |Projected Units |float64 |
| zmean |Mean Height |   |Projected Units |float64 |
| zsd |Standard deviation of height distribution |   |Projected Units |float64 |
| zskew |Skewness of height distribution |   |Dimensionless |float64 |
| zkurt |Kurtosis of height distribution |   |Dimensionless |float64 |
| zentropy |Entropy of height distribution |   |Dimensionless |float64 |
| pzabovezmean |Percentage of returns above zmean |   |Percentage |float64 |
| pzabovex |Percentage of returns above x projection units |   |Percentage |float64 |
| zq5 |5th percentile of height distribution |   |Projected Units |float64 |
| zq10 |10th percentile of height distribution |   |Projected Units |float64 |
| zq15 |15th percentile of height distribution |   |Projected Units |float64 |
| zq20 |20th percentile of height distribution |   |Projected Units |float64 |
| zq25 |25th percentile of height distribution |   |Projected Units |float64 |
| zq30 |30th percentile of height distribution |   |Projected Units |float64 |
| zq35 |35th percentile of height distribution |   |Projected Units |float64 |
| zq40 |40th percentile of height distribution |   |Projected Units |float64 |
| zq45 |45th percentile of height distribution |   |Projected Units |float64 |
| zq50 |50th percentile of height distribution |   |Projected Units |float64 |
| zq55 |55th percentile of height distribution |   |Projected Units |float64 |
| zq60 |60th percentile of height distribution |   |Projected Units |float64 |
| zq65 |65th percentile of height distribution |   |Projected Units |float64 |
| zq70 |70th percentile of height distribution |   |Projected Units |float64 |
| zq75 |75th percentile of height distribution |   |Projected Units |float64 |
| zq80 |80th percentile of height distribution |   |Projected Units |float64 |
| zq85 |85th percentile of height distribution |   |Projected Units |float64 |
| zq90 |90th percentile of height distribution |   |Projected Units |float64 |
| zq95 |95th percentile of height distribution |   |Projected Units |float64 |
| zpcum1 |Cumulative percentage of return in the 1st layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum2 |Cumulative percentage of return in the 2nd layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum3 |Cumulative percentage of return in the 3rd layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum4 |Cumulative percentage of return in the 4th layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum5 |Cumulative percentage of return in the 5th layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum6 |Cumulative percentage of return in the 6th layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum7 |Cumulative percentage of return in the 7th layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum8 |Cumulative percentage of return in the 8th layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| zpcum9 |Cumulative percentage of return in the 9th layer where layers were determined by dividing the range of height measurements into 10 equal intervals after according to Wood et al. |“@article{woods2008predicting,   title={Predicting forest stand variables from LIDAR data in the Great Lakes St. Lawrence Forest of Ontario},   author={Woods, Murray and Lim, K and Treitz, P},   journal={The Forestry Chronicle},   volume={84},   number={6},   pages={827--839},   year={2008},   publisher={NRC Research Press Ottawa, Canada} }”  |Percentage |float64 |
| itot |Sum of intensities for each return |   |Arbitrary based on input file |Int32 |
| imax |Maximum intensity |   |Arbitrary based on input file |Int32 |
| imean |Mean Intensity |   |Arbitrary based on input file |float64 |
| isd |Standard deviation of intensity |   |Arbitrary based on input file |float64 |
| iskew |Skewness of intensity distribution |   |Dimensionless |float64 |
| ikurt |Kurtosis of intensity distribution |   |Dimensionless |float64 |
| ipground |Percentage of intensity returned by points classified as ground |   |Percentage |float64 |
| ipcumzq10 |Percentage of intensity returned below the 10th percentile of height |   |Percentage |float64 |
| ipcumzq30 |Percentage of intensity returned below the 30th percentile of height |   |Percentage |float64 |
| ipcumzq50 |Percentage of intensity returned below the 50th percentile of height |   |Percentage |float64 |
| ipcumzq70 |Percentage of intensity returned below the 70th percentile of height |   |Percentage |float64 |
| ipcumzq90 |Percentage of intensity returned below the 90th percentile of height |   |Percentage |float64 |
| p1th |Percentage of  returns which are 1st returns |   |Percentage |float64 |
| p2th |Percentage of returns which are 2nd returns |   |Percentage |float64 |
| p3th |Percentage of returns which are 3rd returns |   |Percentage |float64 |
| p4th |Percentage of returns which are 4th returns |   |Percentage |float64 |
| p5th |Percentage of returns which are 5th returns |   |Percentage |float64 |
| pground |Percentage of returns which are classified as ground |   |Percentage |float64 |
| n |Number of points |   |Dimensionless |Int32 |
| area |Approximate area of raster |   |Projected Units |float64 |
