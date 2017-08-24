#FIXME JSON file here
# New electron SF
# Check muon SF

import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import os

options = VarParsing ('analysis')
options.parseArguments()


# Determine sample name for MC stitching
sample = (options.inputFiles[0]).split('/')[-1].replace('.txt', '') if len(options.inputFiles) > 0 else ''
if sample=='list': sample = (options.inputFiles[0]).split('/')[-3]

process = cms.Process('ALPHA')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.threshold = 'ERROR'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

# input
# default: if no filelist from command line, run on specified samples

if len(options.inputFiles) == 0:
    process.source = cms.Source('PoolSource',
        fileNames = cms.untracked.vstring(
           #'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016B/SingleMuon/MINIAOD/PromptReco-v1/000/273/013/00000/C09E75A4-3519-E611-8BA9-02163E014476.root', # SingleMuon
           #'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/mc/RunIISpring16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/40000/8219CC5E-F529-E611-A621-14187733AD89.root' # DY
           
           #'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v3/000/284/036/00000/129CD4B5-5D9F-E611-A9AB-02163E014220.root', # SingleMuon
           
           
           
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/E8C064B4-0C8F-E611-B8B8-008CFAFC0500.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/E8F0A7C0-2790-E611-B3D8-20CF305B0581.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/EAF0207C-428F-E611-B174-0090FAA581E4.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/EC726C5F-C090-E611-B6A6-001E67E6F512.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/ECB0D8D4-B68E-E611-9611-0090FAA58434.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/F0FFBA28-3690-E611-85D0-848F69FD4517.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/F4308113-2890-E611-BD8E-001E67E6F85F.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/F627424B-0490-E611-8FB5-3417EBE64BA0.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/F6E7B76F-1390-E611-BC3B-008CFAFBFB94.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/F6F514A9-9B90-E611-8149-0CC47A4DED7E.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/FA79D566-1390-E611-BB88-008CFAFBFB94.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/FACC563A-628F-E611-AB8B-008CFAFBEC9A.root',
           
           
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6A4024AD-C788-E611-B2E6-0090FAA58B94.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6A41A46D-8188-E611-95CD-3417EBE7063F.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6A471EFD-4F87-E611-9327-FA163E622848.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6AE974A5-D489-E611-AE8F-00259021A4A2.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6C0C15DE-8C88-E611-BAF7-FA163E0D4748.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6CA739FD-6C88-E611-8E35-001E677923E6.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6CB07F24-4788-E611-8DAA-FA163E9BA77A.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6CBC4A42-CF88-E611-959B-0025905C95F8.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6CDD978C-D187-E611-A82A-0CC47A009E26.root',
#'dcap://t2-srm-02.lnl.infn.it/pnfs/lnl.infn.it/data/cms//store/data/Run2016D/SingleElectron/MINIAOD/23Sep2016-v1/90000/6CDFF3EB-B487-E611-9F4C-02163E015F9C.root',
           
#           'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/480D3900-8CC0-E611-81E8-001E67504645.root', # DYJetsToLL
          '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/480D3900-8CC0-E611-81E8-001E67504645.root',
           #'/store/data/Run2016D/SingleMuon/MINIAOD/23Sep2016-v1/90000/F627424B-0490-E611-8FB5-3417EBE64BA0.root'
        )
    )
# production: read externally provided filelist
else:
    filelist = open(options.inputFiles[0], 'r').readlines()
    process.source = cms.Source ('PoolSource', fileNames = cms.untracked.vstring(filelist) )

#output
process.TFileService = cms.Service('TFileService',
    fileName = cms.string('output.root' if len(options.outputFile) == 0 else options.outputFile),
    closeFileFast = cms.untracked.bool(True)
)

# Determine whether we are running on data or MC
isData = ('/store/data/' in process.source.fileNames[0])
isCustom = ('GluGluToAToZhToLLBB' in process.source.fileNames[0])
isReHLT = ('_reHLT_' in process.source.fileNames[0])
isReRecoBCD = ('Run2016B-23Sep' in sample or 'Run2016C-23Sep' in sample or 'Run2016D-23Sep' in sample)
isReRecoEF = ('Run2016E-23Sep' in sample or 'Run2016F-23Sep' in sample)
isReRecoG = ('Run2016G-23Sep' in sample)
isReRecoH = ('Run2016H-PromptReco' in sample)
isPromptReco = (('PromptReco' in sample) and (not isReRecoH))
isDibosonInclusive = (True if (sample=='WW_TuneCUETP8M1_13TeV-pythia8-v1' or sample=='WZ_TuneCUETP8M1_13TeV-pythia8-v1' or sample=='ZZ_TuneCUETP8M1_13TeV-pythia8-v1' or sample=='ZZ_TuneCUETP8M1_13TeV-pythia8_ext1-v1') else False)

print 'Running on', ('data' if isData else 'MC'), ', sample is', sample
if isReHLT: print '-> re-HLT sample'
if isDibosonInclusive: print '-> Pythia LO sample'
if isReRecoBCD:
    print "ReReco B-C-D era for JEC on data"
    JECstring = "Summer16_23Sep2016BCDV3_DATA"
elif isReRecoEF:
    print "ReReco E-F era for JEC on data"
    JECstring = "Summer16_23Sep2016EFV3_DATA"
elif isReRecoG:
    print "ReReco G era for JEC on data"
    JECstring = "Summer16_23Sep2016GV3_DATA"
elif isReRecoH:
    print "ReReco H era for JEC on data"
    JECstring = "Summer16_23Sep2016HV3_DATA"
elif isPromptReco:
    print "Prompt reco, old V6 JEC (before dec 2016)"
    JECstring = "Spring16_25nsV6_DATA"
else:
    #print "MC for JEC"
    JECstring = "Spring16_25nsV6_DATA"
#isData = False

#-----------------------#
#        FILTERS        #
#-----------------------#

# JSON filter
import FWCore.PythonUtilities.LumiList as LumiList
if isData:
    #process.source.lumisToProcess = LumiList.LumiList(filename = '%s/src/Analysis/ALPHA/data/JSON/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt' % os.environ['CMSSW_BASE']).getVLuminosityBlockRange() #4.34
    #process.source.lumisToProcess = LumiList.LumiList(filename = '%s/src/Analysis/ALPHA/data/JSON/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt' % os.environ['CMSSW_BASE']).getVLuminosityBlockRange() #6.26
    #process.source.lumisToProcess = LumiList.LumiList(filename = '%s/src/Analysis/ALPHA/data/JSON/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt' % os.environ['CMSSW_BASE']).getVLuminosityBlockRange() #12.9
    #process.source.lumisToProcess = LumiList.LumiList(filename = '%s/src/Analysis/ALPHA/data/JSON/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt' % os.environ['CMSSW_BASE']).getVLuminosityBlockRange() #36.2 fb-1, PromptReco
    process.source.lumisToProcess = LumiList.LumiList(filename = '%s/src/Analysis/ALPHA/data/JSON/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt' % os.environ['CMSSW_BASE']).getVLuminosityBlockRange() #36.814 fb-1, ReReco Moriond

process.counter = cms.EDAnalyzer('CounterAnalyzer',
    lheProduct = cms.InputTag('externalLHEProducer' if not isCustom else 'source'),
    pythiaLOSample = cms.bool(True if isDibosonInclusive else False),
)

# Trigger filter
triggerTag = 'HLT2' if isReHLT else 'HLT'


#process.load('RecoMET.METFilters.metFilters_cff')

process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.muons = cms.InputTag('slimmedMuons')
process.BadPFMuonFilter.PFCandidates = cms.InputTag('packedPFCandidates')
process.load('RecoMET.METFilters.BadPFMuonSummer16Filter_cfi')
process.BadPFMuonSummer16Filter.muons = cms.InputTag("slimmedMuons")
process.BadPFMuonSummer16Filter.PFCandidates = cms.InputTag("packedPFCandidates")

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.muons = cms.InputTag('slimmedMuons')
process.BadChargedCandidateFilter.PFCandidates = cms.InputTag('packedPFCandidates')
process.load('RecoMET.METFilters.BadChargedCandidateSummer16Filter_cfi')
process.BadChargedCandidateSummer16Filter.muons = cms.InputTag('slimmedMuons')
process.BadChargedCandidateSummer16Filter.PFCandidates = cms.InputTag('packedPFCandidates')

#MET corrections and uncertainties
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
if isData:
    jecFile = cms.string('%s/src/Analysis/ALPHA/data/%s/%s_Uncertainty_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring))
else:
    jecFile = cms.string('%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt' % os.environ['CMSSW_BASE'])

runMetCorAndUncFromMiniAOD(process,
                           #metType="PF",
                           #correctionLevel=["T1","Smear"],
                           #computeUncertainties=True,
                           #produceIntermediateCorrections=False,
                           #addToPatDefaultSequence=False,
                           isData=isData,
                           #onMiniAOD=True,
                           #reapplyJEC=reapplyJEC,
                           #reclusterJets=reclusterJets,
                           #jetSelection=jetSelection,
                           #recoMetFromPFCs=recoMetFromPFCs,
                           #autoJetCleaning=jetCleaning,
                           #manualJetConfig=manualJetConfig,
                           #jetFlavor=jetFlavor,
                           #jetCorLabelUpToL3=jetCorLabelL3,
                           #jetCorLabelL3Res=jetCorLabelRes,
                           #jecUnFile=jecFile,
                           #CHS=CHS,
                           #postfix=postfix,
                           )


if isData:
    filterString = "RECO"
else:
    filterString = "PAT"

# Primary vertex
import RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi
process.primaryVertexFilter = cms.EDFilter('GoodVertexFilter',
    vertexCollection = cms.InputTag('offlineSlimmedPrimaryVertices'),
    minimumNDOF = cms.uint32(4) ,
    maxAbsZ = cms.double(24), 
    maxd0 = cms.double(2) 
)


#-----------------------#
#        OBJECTS        #
#-----------------------#

#GLOBALTAG
process.load('Configuration.StandardSequences.Services_cff')#Lisa
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
GT = ''
if isData:          GT = '80X_dataRun2_2016SeptRepro_v7'
elif not(isData):   GT = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
process.GlobalTag = GlobalTag(process.GlobalTag, GT)
print 'GlobalTag', GT

#electron/photon regression modules
from EgammaAnalysis.ElectronTools.regressionWeights_cfi import regressionWeights
process = regressionWeights(process)
process.load('EgammaAnalysis.ElectronTools.regressionApplication_cff')

#electrons upstream modules
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
ele_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff',
                  'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV70_cff',
                  'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring16_GeneralPurpose_V1_cff']
 
for ele_idmod in ele_id_modules:
    setupAllVIDIdsInModule(process,ele_idmod,setupVIDElectronSelection)

#photons upstream modules
switchOnVIDPhotonIdProducer(process, DataFormat.MiniAOD)
ph_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring16_V2p2_cff',
                 'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Spring16_nonTrig_V1_cff']
for ph_idmod in ph_id_modules:
    setupAllVIDIdsInModule(process,ph_idmod,setupVIDPhotonSelection)


#muons upstream modules
process.cleanedMuons = cms.EDProducer('PATMuonCleanerBySegments',
                                      src = cms.InputTag('slimmedMuons'),#('calibratedMuons'),#
                                      preselection = cms.string('track.isNonnull'),
                                      passthrough = cms.string('isGlobalMuon && numberOfMatches >= 2'),
                                      fractionOfSharedSegments = cms.double(0.499)
                                      )

# Jet corrector https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrOnTheFly
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')


#quark gluon likelihood upstream modules
qgDatabaseVersion = 'v2b' # check https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion
from CondCore.CondDB.CondDB_cfi import *
CondDB.connect = cms.string('frontier://FrontierProd/CMS_COND_PAT_000')
QGPoolDBESSource = cms.ESSource('PoolDBESSource',
      CondDB,
      toGet = cms.VPSet()
)
for type in ['AK4PFchs','AK4PFchs_antib']:
    QGPoolDBESSource.toGet.extend(cms.VPSet(cms.PSet(
        record = cms.string('QGLikelihoodRcd'),
        tag    = cms.string('QGLikelihoodObject_'+qgDatabaseVersion+'_'+type),
        label  = cms.untracked.string('QGL_'+type)
    )))
process.load('RecoJets.JetProducers.QGTagger_cfi')
process.QGTagger.srcJets = cms.InputTag('slimmedJets') # Could be reco::PFJetCollection or pat::JetCollection (both AOD and miniAOD)
process.QGTagger.jetsLabel = cms.string('QGL_AK4PFchs') # Other options: see https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion

#https://twiki.cern.ch/twiki/bin/view/CMS/EGMSmearer#ECAL_scale_and_resolution_correc
process.load('EgammaAnalysis.ElectronTools.calibratedElectronsRun2_cfi')
#process.selectedElectrons = cms.EDFilter('PATElectronSelector', 
                                         #src = cms.InputTag('slimmedElectrons'), 
                                         #cut = cms.string('pt > 5 && abs(eta)<2.5') 
                                         #)
calibratedPatElectrons = cms.EDProducer('CalibratedPatElectronProducerRun2',
                                        # input collections
                                        electrons = cms.InputTag('slimmedElectrons'),
                                        gbrForestName = cms.string('gedelectron_p4combination_25ns'),
                                        # data or MC corrections
                                        # if isMC is false, data corrections are applied
                                        isMC = cms.bool(False) if isData else cms.bool(True),
                                        # set to True to get special 'fake' smearing for synchronization. Use JUST in case of synchronization
                                        isSynchronization = cms.bool(False),
                                        correctionFile = cms.string('80X_DCS05July_plus_Golden22')
                                        )

## Update PAT jets

#from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

### b-tag discriminators
#bTagDiscriminators = [
#    'pfTrackCountingHighEffBJetTags',
#    'pfTrackCountingHighPurBJetTags',
#    'pfJetProbabilityBJetTags',
#    'pfJetBProbabilityBJetTags',
#    'pfSimpleSecondaryVertexHighEffBJetTags',
#    'pfSimpleSecondaryVertexHighPurBJetTags',
#    'pfCombinedSecondaryVertexV2BJetTags',
#    'pfCombinedInclusiveSecondaryVertexV2BJetTags',
#    'pfCombinedMVAV2BJetTags',
#    'pfBoostedDoubleSecondaryVertexAK8BJetTags'
#]

#from PhysicsTools.PatAlgos.tools.jetTools import *
### Update the slimmedJets in miniAOD: corrections from the chosen Global Tag are applied and the b-tag discriminators are re-evaluated
#updateJetCollection(
#    process,
#    jetSource = cms.InputTag('slimmedJets'),
#    jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
#    btagDiscriminators = bTagDiscriminators
#)





#-----------------------#
#        NTUPLE         #
#-----------------------#

process.ntuple = cms.EDAnalyzer('Diboson',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        lheProduct = cms.InputTag('externalLHEProducer' if not isCustom else 'source'),
        genParticles = cms.InputTag('prunedGenParticles'),
        pdgId = cms.vint32(1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 23, 24, 25, 36, 39, 1000022, 9100000, 9000001, 9000002, 9100012, 9100022, 9900032, 1023),
        samplesDYJetsToLL = cms.vstring(
#            'DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'DYBBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v2',
#            'DYBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
        ),
        samplesZJetsToNuNu = cms.vstring(
#            'DYJetsToNuNu_PtZ-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1',
#            'DYJetsToNuNu_PtZ-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1',
#            'DYJetsToNuNu_PtZ-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1',
#            'DYJetsToNuNu_PtZ-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1',
#            'ZJetsToNuNu_HT-100To200_13TeV-madgraph_ext1-v1',
#            'ZJetsToNuNu_HT-200To400_13TeV-madgraph_ext1-v1',
#            'ZJetsToNuNu_HT-400To600_13TeV-madgraph_ext1-v1',
#            'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1',
#            'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v3',
#            'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_ext1-v1',
#            'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1',
        ),
        samplesWJetsToLNu = cms.vstring(
#            'WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1',
#            'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
            ##'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
#            'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1',
            #'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v2',
#            'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
#            'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0-v1',
        ),
        samplesDir = cms.string('%s/src/Analysis/ALPHA/data/Stitch/' % os.environ['CMSSW_BASE']),
        sample = cms.string( sample ),
        ewkFile = cms.string('%s/src/Analysis/ALPHA/data/scalefactors_v4.root' % os.environ['CMSSW_BASE']),
        applyEWK = cms.bool(True if sample.startswith('DYJets') or sample.startswith('WJets') else False),
        applyTopPtReweigth = cms.bool(True if sample.startswith('TT_') else False),
        pythiaLOSample = cms.bool(True if isDibosonInclusive else False),
    ),
    pileupSet = cms.PSet(
        pileup = cms.InputTag('slimmedAddPileupInfo'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        dataFileName     = cms.string('%s/src/Analysis/ALPHA/data/PU_69200_ReReco.root' % os.environ['CMSSW_BASE']),#updated
        dataFileNameUp   = cms.string('%s/src/Analysis/ALPHA/data/PU_72380_ReReco.root' % os.environ['CMSSW_BASE']),#updated
        dataFileNameDown = cms.string('%s/src/Analysis/ALPHA/data/PU_66020_ReReco.root' % os.environ['CMSSW_BASE']),#updated
        mcFileName = cms.string('%s/src/Analysis/ALPHA/data/PU_MC_Moriond17.root' % os.environ['CMSSW_BASE']),#updated
        dataName = cms.string('pileup'),
        #mcName = cms.string('2016_25ns_SpringMC_PUScenarioV1'),#updated
        mcName = cms.string('2016_25ns_Moriond17MC_PoissonOOTPU'),#updated
    ),
    triggerSet = cms.PSet(
        trigger = cms.InputTag('TriggerResults', '', triggerTag),
        paths = cms.vstring('HLT_Mu45_eta2p1_v', 'HLT_Mu50_v', 'HLT_TkMu50_v', 'HLT_IsoMu20_v', 'HLT_IsoTkMu20_v', 'HLT_IsoMu24_v', 'HLT_IsoTkMu24_v', 'HLT_Mu27_TkMu8_v', 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v', 'HLT_Ele105_CaloIdVT_GsfTrkIdT_v', 'HLT_Ele115_CaloIdVT_GsfTrkIdT_v', 'HLT_Ele23_WPLoose_Gsf_v', 'HLT_Ele27_WPLoose_Gsf_v', 'HLT_Ele27_WPTight_Gsf_v', 'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v', 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v', 'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v', 'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v', 'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v', 'HLT_PFMET120_BTagCSV_p067_v', 'HLT_PFMET170_NotCleaned_v', 'HLT_PFMET170_NoiseCleaned_v', 'HLT_PFMET170_JetIdCleaned_v', 'HLT_PFMET170_HBHECleaned_v', 'HLT_DoublePhoton60_v',),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter'),
        badPFMuonFilter = cms.InputTag("BadPFMuonFilter"),
        badChCandFilter = cms.InputTag("BadChargedCandidateFilter"),
    ),
    electronSet = cms.PSet(
        #electrons = cms.InputTag('selectedElectrons'),
        electrons = cms.InputTag('slimmedElectrons'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        eleVetoIdMap = cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-veto'),
        eleLooseIdMap = cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-loose'),
        eleMediumIdMap = cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-medium'),
        eleTightIdMap = cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight'),
        eleHEEPIdMap = cms.InputTag('egmGsfElectronIDs:heepElectronID-HEEPV70'),
        eleMVANonTrigMediumIdMap = cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp90'),
        eleMVANonTrigTightIdMap = cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
        eleMVATrigMediumIdMap = cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp90'), ### NOTE -> SAME AS NON-TRIG IN 2017
        eleMVATrigTightIdMap = cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp80'), ### NOTE -> SAME AS NON-TRIG IN 2017
        eleEcalRecHitCollection = cms.InputTag("reducedEgamma:reducedEBRecHits"),
        eleSingleTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/SingleEleTriggerEff.root' % os.environ['CMSSW_BASE']),
        eleVetoIdFileName = cms.string('%s/src/Analysis/ALPHA/data/eleVetoIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        eleLooseIdFileName = cms.string('%s/src/Analysis/ALPHA/data/eleLooseIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        eleMediumIdFileName = cms.string('%s/src/Analysis/ALPHA/data/eleMediumIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        eleTightIdFileName = cms.string('%s/src/Analysis/ALPHA/data/eleTightIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        eleMVATrigMediumIdFileName = cms.string('%s/src/Analysis/ALPHA/data/eleMVA90IDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        eleMVATrigTightIdFileName = cms.string('%s/src/Analysis/ALPHA/data/eleMVA80IDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        eleRecoEffFileName = cms.string('%s/src/Analysis/ALPHA/data/eleRecoSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        electron1id = cms.int32(0), # 0: veto, 1: loose, 2: medium, 3: tight, 4: HEEP, 5: MVA medium nonTrig, 6: MVA tight nonTrig, 7: MVA medium Trig, 8: MVA tight Trig
        electron2id = cms.int32(0),
        electron1pt = cms.double(10),
        electron2pt = cms.double(10),
    ),
    muonSet = cms.PSet(
        muons = cms.InputTag('cleanedMuons'),#('slimmedMuons'),#
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        muonTrkFileName = cms.string('%s/src/Analysis/ALPHA/data/TrkEff.root' % os.environ['CMSSW_BASE']),
        muonIdFileName = cms.string('%s/src/Analysis/ALPHA/data/MuonIdEfficienciesAndSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        muonIsoFileName = cms.string('%s/src/Analysis/ALPHA/data/MuonIsoEfficienciesAndSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        muonTrkHighptFileName = cms.string('%s/src/Analysis/ALPHA/data/tkhighpt_2016full_absetapt.root' % os.environ['CMSSW_BASE']),
        muonTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/MuonTrigEfficienciesAndSF_MORIOND17_Period34.root' % os.environ['CMSSW_BASE']),
        doubleMuonTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root' % os.environ['CMSSW_BASE']),#FIXME -> obsolete
        muon1id = cms.int32(0), # 0: tracker high pt muon id, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(0),
        muon1iso = cms.int32(0), # 0: trk iso (<0.1), 1: loose (<0.25), 2: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(0),
        muon1pt = cms.double(20.),
        muon2pt = cms.double(20.),
        useTuneP = cms.bool(True),
        doRochester = cms.bool(False),
    ),
    muonLooseSet = cms.PSet(
        muons = cms.InputTag('cleanedMuons'),#('slimmedMuons'),#
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        muonTrkFileName = cms.string('%s/src/Analysis/ALPHA/data/TrkEff.root' % os.environ['CMSSW_BASE']),
        muonIdFileName = cms.string('%s/src/Analysis/ALPHA/data/MuonIdEfficienciesAndSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        muonIsoFileName = cms.string('%s/src/Analysis/ALPHA/data/MuonIsoEfficienciesAndSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        muonTrkHighptFileName = cms.string('%s/src/Analysis/ALPHA/data/tkhighpt_2016full_absetapt.root' % os.environ['CMSSW_BASE']),
        muonTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/MuonTrigEfficienciesAndSF_MORIOND17_Period34.root' % os.environ['CMSSW_BASE']),
        doubleMuonTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root' % os.environ['CMSSW_BASE']),#FIXME -> obsolete
        muon1id = cms.int32(1), # 0: tracker high pt muon id, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(1),
        muon1iso = cms.int32(1), # 0: trk iso (<0.1), 1: loose (<0.25), 2: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(1),
        muon1pt = cms.double(10.),
        muon2pt = cms.double(10.),
        useTuneP = cms.bool(False),
        doRochester = cms.bool(False),
    ),
    tauSet = cms.PSet(
        taus = cms.InputTag('slimmedTaus'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        taupt = cms.double(18.),
        taueta = cms.double(2.3),
        tauIdByDecayMode = cms.int32(1),# 0: not set, 1: old, 2: new
        tauIdByDeltaBetaIso = cms.int32(1),# 0: not set, 1: loose, 2: medium, 3: tight
        tauIdByMVAIso = cms.int32(0),# 0: not set, 1: V loose, 2: loose, 3: medium, 4: tight, 5: V tight
        tauIdByMuonRejection = cms.int32(0),# 0: not set, 1: loose, 2: tight
        tauIdByElectronRejection = cms.int32(0),# 0: not set, 1: V loose, 2: loose, 3: medium, 4: tight
    ),
    photonSet = cms.PSet(
        photons = cms.InputTag('slimmedPhotons'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        phoLooseIdMap = cms.InputTag('egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-loose'),
        phoMediumIdMap = cms.InputTag('egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-medium'),
        phoTightIdMap = cms.InputTag('egmPhotonIDs:cutBasedPhotonID-Spring16-V2p2-tight'),
        phoMVANonTrigMediumIdMap = cms.InputTag('egmPhotonIDs:mvaPhoID-Spring16-nonTrig-V1-wp90'),
        phoEcalRecHitCollection = cms.InputTag("reducedEgamma:reducedEBRecHits"),
        phoLooseIdFileName = cms.string('%s/src/Analysis/ALPHA/data/phoLooseIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        phoMediumIdFileName = cms.string('%s/src/Analysis/ALPHA/data/phoMediumIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        phoTightIdFileName = cms.string('%s/src/Analysis/ALPHA/data/phoTightIDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        phoMVANonTrigMediumIdFileName = cms.string('%s/src/Analysis/ALPHA/data/phoMVA90IDSF_MORIOND17.root' % os.environ['CMSSW_BASE']),
        photonid = cms.int32(1), # 1: loose, 2: medium, 3: tight, 4:MVA NonTrig medium
        photonpt = cms.double(15.),
    ),
    jetSet = cms.PSet(
        jets = cms.InputTag('slimmedJets'),#('slimmedJetsAK8'), #selectedPatJetsAK8PFCHSPrunedPacked
        jetid = cms.int32(1), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(30.),
        jet2pt = cms.double(30.),
        jeteta = cms.double(2.5),
        addQGdiscriminator = cms.bool(True),
        recalibrateJets = cms.bool(True),
        recalibrateMass = cms.bool(False),
        recalibratePuppiMass = cms.bool(False),
        smearJets = cms.bool(True),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        rho = cms.InputTag('fixedGridRhoFastjetAll'),        
        jecUncertaintyDATA = cms.string('%s/src/Analysis/ALPHA/data/%s/%s_Uncertainty_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring)),#updating
        jecUncertaintyMC = cms.string('%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt' % os.environ['CMSSW_BASE']),#updating
        jecCorrectorDATA = cms.vstring(#updating
            '%s/src/Analysis/ALPHA/data/%s/%s_L1FastJet_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L2Relative_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L3Absolute_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L2L3Residual_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
        ),
        jecCorrectorMC = cms.vstring(#updating!!!
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt' % os.environ['CMSSW_BASE'],
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt' % os.environ['CMSSW_BASE'],
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt' % os.environ['CMSSW_BASE'],
        ),
        massCorrectorDATA = cms.vstring(#updating!!!
            '%s/src/Analysis/ALPHA/data/%s/%s_L2Relative_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L3Absolute_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L2L3Residual_AK4PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
        ),
        massCorrectorMC = cms.vstring(#updating!!!
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt' % os.environ['CMSSW_BASE'],
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt' % os.environ['CMSSW_BASE'],
        ),
        massCorrectorPuppi = cms.string('%s/src/Analysis/ALPHA/data/puppiCorrSummer16.root' % os.environ['CMSSW_BASE']),#updating
        reshapeBTag = cms.bool(True),
        btag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        btagDB = cms.string('%s/src/Analysis/ALPHA/data/CSVv2_Moriond17_B_H.csv' % os.environ['CMSSW_BASE']),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETs','','ALPHA'),#("patPFMetT1Smear"),#
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('%s/src/Analysis/ALPHA/data/recoilfit_gjetsMC_Zu1_pf_v5.root' % os.environ['CMSSW_BASE']),
        metRecoilData = cms.string('%s/src/Analysis/ALPHA/data/recoilfit_gjetsData_Zu1_pf_v5.root' % os.environ['CMSSW_BASE']),
        metTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/MET_trigger_eff_data_SingleMuRunBH.root' % os.environ['CMSSW_BASE']),
        jerNameRes = cms.string('%s/src/Analysis/ALPHA/data/JER/Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt' % os.environ['CMSSW_BASE']),#v10 is the latest
        jerNameSf = cms.string('%s/src/Analysis/ALPHA/data/JER/Spring16_25nsV10_MC_SF_AK4PFchs.txt' % os.environ['CMSSW_BASE']),#v10 is the latest
    ),
    fatJetSet = cms.PSet(
        jets = cms.InputTag('slimmedJetsAK8'),#('slimmedJetsAK8'), #selectedPatJetsAK8PFCHSPrunedPacked
        jetid = cms.int32(1), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(150.),
        jet2pt = cms.double(150.),
        jeteta = cms.double(2.5),
        addQGdiscriminator = cms.bool(True),
        recalibrateJets = cms.bool(True),
        recalibrateMass = cms.bool(True),
        recalibratePuppiMass = cms.bool(True),
        smearJets = cms.bool(True),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        rho = cms.InputTag('fixedGridRhoFastjetAll'),        
        jecUncertaintyDATA = cms.string('%s/src/Analysis/ALPHA/data/%s/%s_Uncertainty_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring)),#updating!! Puppi or CHS?
        jecUncertaintyMC = cms.string('%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK8PFchs.txt' % os.environ['CMSSW_BASE']),#updating!! Puppi or CHS?
        jecCorrectorDATA = cms.vstring(#updating
            '%s/src/Analysis/ALPHA/data/%s/%s_L1FastJet_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L2Relative_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L3Absolute_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L2L3Residual_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
        ),
        jecCorrectorMC = cms.vstring(#updating!!!
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK8PFchs.txt' % os.environ['CMSSW_BASE'],
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK8PFchs.txt' % os.environ['CMSSW_BASE'],
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK8PFchs.txt' % os.environ['CMSSW_BASE'],
        ),
        massCorrectorDATA = cms.vstring(#updating
            '%s/src/Analysis/ALPHA/data/%s/%s_L2Relative_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L3Absolute_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
            '%s/src/Analysis/ALPHA/data/%s/%s_L2L3Residual_AK8PFchs.txt' % (os.environ['CMSSW_BASE'], JECstring, JECstring),
        ),
        massCorrectorMC = cms.vstring(#updating
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK8PFchs.txt' % os.environ['CMSSW_BASE'],
            '%s/src/Analysis/ALPHA/data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK8PFchs.txt' % os.environ['CMSSW_BASE'],
        ),
        massCorrectorPuppi = cms.string('%s/src/Analysis/ALPHA/data/puppiCorrSummer16.root' % os.environ['CMSSW_BASE']),#updating
        reshapeBTag = cms.bool(True),
        btag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        btagDB = cms.string('%s/src/Analysis/ALPHA/data/CSVv2_Moriond17_B_H.csv' % os.environ['CMSSW_BASE']),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETs','','ALPHA'),#("patPFMetT1Smear"),#
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string(''),
        metRecoilData = cms.string(''),
        metTriggerFileName = cms.string('%s/src/Analysis/ALPHA/data/MET_trigger_eff_data_SingleMuRunBH.root' % os.environ['CMSSW_BASE']),
        jerNameRes = cms.string('%s/src/Analysis/ALPHA/data/JER/Spring16_25nsV10_MC_PtResolution_AK8PFchs.txt' % os.environ['CMSSW_BASE']),#v10 is the latest
        jerNameSf = cms.string('%s/src/Analysis/ALPHA/data/JER/Spring16_25nsV10_MC_SF_AK8PFchs.txt' % os.environ['CMSSW_BASE']),#v10 is the latest
    ),
    writeNElectrons = cms.int32(0),
    writeNMuons = cms.int32(0),
    writeNLeptons = cms.int32(2),
    writeNTaus = cms.int32(0),
    writeNPhotons = cms.int32(0),
    writeNJets = cms.int32(0),
    writeNFatJets = cms.int32(1),
    histFile = cms.string('%s/src/Analysis/ALPHA/data/HistList.dat' % os.environ['CMSSW_BASE']),
    verbose  = cms.bool(False),
)


#process.output = cms.OutputModule('PoolOutputModule',
#  splitLevel = cms.untracked.int32(0),
#  fileName = cms.untracked.string('deleteme.root'),
#  dataset = cms.untracked.PSet(
#    filterName = cms.untracked.string(''),
#    dataTier = cms.untracked.string('')
#  )
#)

if isData:
    process.seq = cms.Sequence(
        process.counter *
        process.BadPFMuonFilter *
        process.BadChargedCandidateFilter *
        process.fullPatMetSequence *#L
        
        process.primaryVertexFilter *
        process.egmGsfElectronIDSequence *
        process.calibratedPatElectrons *
        process.egmPhotonIDSequence *
        process.cleanedMuons *
        #process.ak4PFL2L3ResidualCorrectorChain *
        process.QGTagger *
        process.ntuple
    )
else:
    process.seq = cms.Sequence(
        process.counter *
        process.BadPFMuonFilter * process.BadPFMuonSummer16Filter *
        process.BadChargedCandidateFilter * process.BadChargedCandidateSummer16Filter *
        process.fullPatMetSequence *#L
        process.primaryVertexFilter *
        #process.EGMenergyCorrection *
        process.regressionApplication *
        process.egmGsfElectronIDSequence *
        process.calibratedPatElectrons *
        process.egmPhotonIDSequence *
        process.cleanedMuons *
        #process.ak4PFL2L3ResidualCorrectorChain *
        process.QGTagger *
        process.ntuple
    )

#process.seq = cms.Sequence( process.counter )

process.p = cms.Path(process.seq)
