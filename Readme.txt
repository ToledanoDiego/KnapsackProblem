 ########## DESCRIPTION #########

This directory contains the MSc Fianl Report and the supplemental files for the Robust Knapsack Problem considered in the following paper

Toledano, D.,
"Bilevel and Decoupling Approaches for the Robust Knapsack Problem",
London: King's College London, 2021.

 ########## INSTANCES #########

Folder Instances contains the 300 instances considered in the paper. 
Each file has name 
	RKP_c_n_class_ind.txt 
where:
-- c denotes the knapsack capacity
-- n denotes the number of items
-- class denotes the type of instances, as follows:
    (i) 	1	uncorrelated
    (ii) 	2	weakly correlated
    (iii)	3 	strongly correlated
    (iv) 	4	inverse correlated
    (v) 	5	subset sum
-- ind is a counter between 1 and 10 

The format of each file is as follows:
-- number of items n
-- n lines, one per item, each containing:
	(i)   a progressive index
	(ii)  the profit of the item
	(iii) the nominal weight of the item
	(iv)  the robust weight of the item
-- the last line contains the capacity of the knapsack

 ########## PROCESSING #########

Folder Processing contains folders for different interogations axis for this project while each folder contains files.

Each file has a name
	abMeans.txt
where:
-- a denotes the value we are grouping our means by, each can be:
	(i)		Gamma		    Means have been grouped by the number of items that may change their weight
	(ii)	Perturbation    Means have been grouped by the percent of robustness
	(iii)	Nothing		    Means have not been grouped by
-- b denotes the Knapsack model used, each can be:
	(i)     B-LRKP	Bi-Level Robust Knapsack Problem
	(ii)    DB&BRKP Decoupling Branch & Bound Robust Knapsack Problem
	(iii)   M0-1KP	Mixed 0-1 Knapsack Problem
	(iv)    MIKP	Mixed Integer Knapsack Problem
	(v)     RIKP	Robust Integer Knapsack Problem
	(vi)    RKP 	Robust Knapsack Problem
	(vii)	RM0-1KP	Robust Mixed 0-1 Knapsack Problem 
	(viii)  RMIKP	Robust Mixed Integer Knapsack Problem
	(ix) 	0-1KP	0-1 Knapsack Problem
	(x)     G0-1KP	Greedy 0-1 Knapsack Problem
	(xi)    IKP		Integer Knapsack Problem

The format of each file is as follows:
-- n lines, one per group
	Each such line contains:
		(i)		the name of the Knapsack model used if no group is needed, the percent of the value instances have been grouped by, the name of the instance otherwise
		(ii)	the mean optimal solution value of the instance or groupe stated above
		(iii)	the mean time to find optimal solutions of the instance or groupe stated above

 ########## Report #########
 
Folder Report contains theMSc Final Report of this project.

 ########## SOLUTIONS #########

Folder Solutions contains the solutions for different model of the Knapsack Problem,
some of them are testing different value of \Gamma \in \{10, 20, 50, 100\} and of the Robustness \in \{10, 20, 50, 100\}

Each file has name 
	m_a%_b%.txt
where:
-- m denotes the Knapsack model used, each can be:
	(i)     B-LRKP	Bi-Level Robust Knapsack Problem
	(ii)    DB&BRKP Decoupling Branch & Bound Robust Knapsack Problem
	(iii)   M0-1KP	Mixed 0-1 Knapsack Problem
	(iv)    MIKP	Mixed Integer Knapsack Problem
	(v)     RIKP	Robust Integer Knapsack Problem
	(vi)    RKP 	Robust Knapsack Problem
	(vii)	RM0-1KP	Robust Mixed 0-1 Knapsack Problem 
	(viii)  RMIKP	Robust Mixed Integer Knapsack Problem
	(ix) 	0-1KP	0-1 Knapsack Problem
	(x)     G0-1KP	Greedy 0-1 Knapsack Problem
	(xi)    IKP		Integer Knapsack Problem
-- a denotes the max number of items that may change their weight if alone, the percent of robustness otherwise
-- b denotes the max number of items that may change their weight

The format of each file is as follows:
-- 300 lines, one for each instances
	Each such line contains:
		(i)		the name of the instance
		(ii)	the optimal solution value
		(iii)	the time to find it
		(iv)	the list of items that is inserted in the optimal solution with their quantity if needed.
		
 ########## Visualization #########
 
Folder Visualization contains graphs for different interogations axis for this project while each folder contains files.

Each file has a name
	aMeansb.txt
	
where:
-- a the Knapsack model used, each can be:
	(i)     B-LRKP	Bi-Level Robust Knapsack Problem
	(ii)    DB&BRKP Decoupling Branch & Bound Robust Knapsack Problem
	(iii)   M0-1KP	Mixed 0-1 Knapsack Problem
	(iv)    MIKP	Mixed Integer Knapsack Problem
	(v)     RIKP	Robust Integer Knapsack Problem
	(vi)    RKP 	Robust Knapsack Problem
	(vii)	RM0-1KP	Robust Mixed 0-1 Knapsack Problem 
	(viii)  RMIKP	Robust Mixed Integer Knapsack Problem
	(ix) 	0-1KP	0-1 Knapsack Problem
	(x)     G0-1KP	Greedy 0-1 Knapsack Problem
	(xi)    IKP		Integer Knapsack Problem
-- b denotes the value we are grouping our means by, each can be:
	(i)		Gamma		    Means have been grouped by the number of items that may change their weight
	(ii)	Perturbation    Means have been grouped by the percent of robustness
	(iii)	Nothing		    Means have not been grouped by