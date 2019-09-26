from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SingleMu_0PU_MC_50k_step3_noCut_1'
config.General.workArea = 'crab_SingleMu'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_RECOSIM_PAT_VALIDATION_DQM.py'
#config.JobType.maxMemoryMB = 8000
#config.JobType.maxJobRuntimeMin = 2700

#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.inputDataset = '/SingleMu_0PU_50k/lian-CRAB3_SingleMu_MC_generation_50k_step2-05df1edc2ea10de838194d35dea92f84/USER'
#config.Data.inputDataset = '/SingleElectron_test_LIAN/lian-CRAB3_SingleElectron_MC_generation_step1_test_2-78ab203945b89797cc0d87e23054e0bd/USER'
#config.Data.ignoreLocality = True
#https://cmsweb.cern.ch/das/request?input=%2FSingleElectron_test_LIAN%2Flian-CRAB3_SingleElectron_MC_generation_step1_test_2-78ab203945b89797cc0d87e23054e0bd%2FUSER&instance=prod%2Fphys03
#config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.totalUnits = 100
config.Data.outLFNDirBase = '/store/user/lian/'
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_SingleMu_MC_50k_step3_noCut_1'

#config.Site.whitelist = ['T2_US_Purdue','T1_US_FNAL','T2_US_Nebraska']
config.Site.storageSite = 'T3_US_FNALLPC'
