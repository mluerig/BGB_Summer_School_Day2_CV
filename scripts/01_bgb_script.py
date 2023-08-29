# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:51:33 2023

@author: mluerig
"""

#%% import packages

import phenopype as pp
import os

#%% set directory paths

os.chdir(r"D:\workspace\python\phenopype_projects\benthic_inverts")
image_dir = r"data_raw"
template_path = r"phenopype_templates\pp_mzb_template1_mod.yaml"

#%% run analysis

## create project
proj = pp.Project(r"phenopype/BGB1") ## overwrite=True

## add photos (every image will get its own sub-folder)
proj.add_files(image_dir = image_dir)

## add configuration template to every folder
proj.add_config(template_path=template_path, tag="v1")

## read size/color reference 
proj.add_reference(proj.dir_paths[0], "scale1")

## run image processing in a for-loop for every image
for path in proj.dir_paths:
    pp.Pype(path, tag="v1", zoom_memory=True)

## collect results and store in folder "<project-root>/results/annotations"
proj.collect_results("v1", "canvas", "canvas_v1", overwrite=True)
proj.collect_results("v1", "reference", "reference_v1", overwrite=True)
proj.collect_results("v1", "shape_features", "shape_features_v1", overwrite=True)
proj.collect_results("v1", "texture_features", "texture_features_v1", overwrite=True)


