import numpy as np
import pandas as pd

from ConfigSpace import ConfigurationSpace
from ConfigSpace.hyperparameters import CategoricalHyperparameter, UniformFloatHyperparameter, UniformIntegerHyperparameter

#now they are going to make the dimensions for XGBoost

#the number of trees in our random forest
num_trees = UniformIntegerHyperparameter("num_trees", 10, 50, default_value = 10)

#number of features which I think are branches
max_features = UniformIntegerHyperparameter("max_features", 1, 100, default_value = 1)

#not sure what this 
min_weight_frac_leaf = UniformFloatHyperparameter("min_weight_frac_leaf", 0.0, 0.5, default_value = 0.0)

#not sure what this is
min_samples_to_split = UniformIntegerHyperparameter("min_samples_to_split", 1, 20, default_value = 1)

#not sure what this is
min_samples_in_leaf = UniformIntegerHyperparameter("min_samples_in_leaf", 1, 20, default_value = 1)

#not sure what this is
max_leaf_nodes = UniformIntegerHyperparameter("max_leaf_nodes", 10, 1000, default_value = 100)

#then they are going to add categorical dimensions

#not sure what this is but it looks like it is doing boostrapping (obviously)
do_boostarpping = CategoricalHyperparameter("do_bootsrapping", ['true', 'false'], default_value = "true")

#this looks like what kind of optimization we will use but I'm not sure
criterion = CategoricalHyperparameter("criterion", ["mse", "mae"], default_value = "mse")

#then they are going to make a criterion space
cs = ConfigurationSpace()

#add those hyperparameters
cs.add_hyperparameters([num_trees, min_weight_frac_leaf, max_features, min_samples_to_split, min_samples_in_leaf, max_leaf_nodes,
                        criterion, do_boostarpping])

#then make the configuration space (not sure what this is)
cs.sample_configuration()

#make a class for optimization
class Optimizer:
    
    #algo sccore is the score we will give the configuration
    #max_iter is the maximum number of training to perform
    #max_intensification is the maximal number of randomly generated configurations
    #model is the calss of internal model used as a score estimator
    #cs the configuration space
    
    def __init__(self, algo_score, max_iter, max_intensification, model, cs):
        
        self.traj = []
        self.trajectory = []
        self.cfgs = []
        self.scores = {}
        self.best_cfg = None
        self.best_score = None
        
        #passed variables
        self.algo_score = algo_score
        self.max_iter = max_iter
        self.max_intensification = max_intensification
        self.internal_model = model()
        self.cs = cs
        
    #this function will convert the configts into pandas dataframe
    def cfg_to_dft(self, cfgs):
        
        #not sure what this is but its definitely making a dictionary
        #it looks like we group the data into dictionary first
        cfgs = [dict(cfg) for cfg in cfgs]
        
        #then make that dictionary into a dataframe
        dtf = pd.DataFrame(cfgs)
        
        return dtf
    
    #this will get the internal score estimator
    def optimize(self):
        
        #not sure what his is
        cfg = self.cs.sample_configuration()
        
        #then we want to append the data
        self.cfgs.append(cfg)
        
        #then add it in the trajectory
        self.trajectory.append(cfg)
        
        #then do the run
        score = self.algo_score(cfg)
        
        #add the score in 
        self.scores[cfg] = score
        
        #save that as the best one
        self.best_cfg = cfg
        
        #then save the best score
        self.best_score = score
        
        #then get the dataframe
        dtf = self.cfg_to_dtf(self.cfgs)
        
        
        
        
        
        
        