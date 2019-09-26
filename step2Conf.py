from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SingleMu_0PU_MC_generation_50k_step2'
config.General.workArea = 'crab_SingleMu'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT.py'
#config.JobType.maxMemoryMB = 6000

#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.inputDataset = '/SingleMu_0PU_50k/lian-CRAB3_SingleMu_MC_step1_50k-8d170e84521749aa4d804a63ec84a1ee/USER'
config.Data.unitsPerJob = 1
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.totalUnits = 100
config.Data.outLFNDirBase = '/store/user/%s' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_SingleMu_MC_generation_50k_step2'

config.Site.storageSite = 'T3_US_FNALLPC'
