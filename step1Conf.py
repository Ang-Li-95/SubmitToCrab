from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SingleMu_0PU_MC_step1_50k'
config.General.workArea = 'crab_SingleMu'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SingleMuPt10_pythia8_cfi_GEN_SIM.py'

config.Data.outputPrimaryDataset = 'SingleMu_0PU_50k'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
#NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits = 50000
config.Data.outLFNDirBase = '/store/user/%s' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_SingleMu_MC_step1_50k'

config.Site.storageSite = 'T3_US_FNALLPC'
