#! /usr/bin/env python

import os, multiprocessing
import copy
import math
from array import array
from ROOT import gROOT, TFile, TTree, TObject, TH1, TH1F, AddressOf

# Import objects (structs)
gROOT.ProcessLine('.L %s/src/Analysis/ALPHA/plugins/Objects.h+' % os.environ['CMSSW_BASE'])
from ROOT import LeptonType, JetType, FatJetType, MEtType, MEtFullType, CandidateType, LorentzType

import argparse

parser = argparse.ArgumentParser(description='skim the LSF outputs into another tree')
parser.add_argument('folder', help='the folder containing the LSF output')
args = parser.parse_args()

if not os.path.exists(os.path.expandvars(args.folder)):
    print '--- ERROR ---'
    print '  \''+args.folder+'\' path not found'
    print '  please point to the correct path to the folder containing the LSF output' 
    print 
    exit()

jobs = []


# Struct
Lepton1 = LeptonType()
Lepton2 = LeptonType()
FatJet1 = FatJetType()
V = CandidateType()
X = CandidateType()
MEt = MEtType()

# New variables
EventNumber = array('l', [0])
EventWeight = array('f', [0])
RunNumber = array('l', [0])
LumiNumber = array('l', [0])
isZtoEE = array('b', [0])
isZtoMM = array('b', [0])
isZtoNN = array('b', [0])
isMC = array('b', [0])
FatJet1_pt = array('f', [0])
FatJet1_softdropPuppiMass = array('f', [0])
FatJet1_softdropPuppiMassCorr = array('f', [0])
FatJet1_softdropPuppiMassCorrNotSmeared = array('f', [0])
FatJet1_puppiTau21 = array('f', [0])
FatJet1_ddtTau21 = array('f', [0])
FatJet1_CSV = array('f', [-1000])
FatJet1_CSVR = array('f', [-1000])
FatJet1_CSV1 = array('f', [-1000])
FatJet1_CSV2 = array('f', [-1000])
FatJet1_CSVR1 = array('f', [-1000])
FatJet1_CSVR2 = array('f', [-1000])
V_mass = array('f', [0])
V_pt = array('f', [0])
MEt_pt = array('f', [0])
X_mass = array('f', [0])
X_tmass = array('f', [0])

def skim(name):
        
    oldFile = TFile(name, "READ")
    oldTree = oldFile.Get("ntuple/tree")
    oldTree.SetBranchAddress("Lepton1", AddressOf(Lepton1,  "pt") );
    oldTree.SetBranchAddress("Lepton2", AddressOf(Lepton2,  "pt") );
    oldTree.SetBranchAddress("FatJet1", AddressOf(FatJet1,  "pt") );
    oldTree.SetBranchAddress("V",       AddressOf(V, "pt")        );
    oldTree.SetBranchAddress("X",       AddressOf(X, "pt")        );
    oldTree.SetBranchAddress("MEt",     AddressOf(MEt, "pt")      );
    
    print 'skimming file',oldFile.GetName(),'\tevents =',oldTree.GetEntries(),'\tweight =',oldTree.GetWeight()
    
    newFile = TFile("Skim/"+name, "RECREATE")
    newFile.cd()
    newTree = TTree("alpha", "alpha")
    
    EventNumberBranch = newTree.Branch('EventNumber', EventNumber, 'EventNumber/F')
    EventWeightBranch = newTree.Branch('EventWeight', EventWeight, 'EventWeight/F')
    RunNumberBranch = newTree.Branch('RunNumber', RunNumber, 'RunNumber/F')
    LumiNumberBranch = newTree.Branch('LumiNumber', LumiNumber, 'LumiNumber/F')
    isZtoEEBranch = newTree.Branch('isZtoEE', isZtoEE, 'isZtoEE/O')
    isZtoMMBranch = newTree.Branch('isZtoMM', isZtoMM, 'isZtoMM/O')
    isZtoNNBranch = newTree.Branch('isZtoNN', isZtoNN, 'isZtoNN/O')
    isMCBranch = newTree.Branch('isMC', isMC, 'isMC/O')
    FatJet1_ptBranch = newTree.Branch('FatJet1_pt', FatJet1_pt, 'FatJet1_pt/F')
    FatJet1_softdropPuppiMassBranch = newTree.Branch('FatJet1_softdropPuppiMass', FatJet1_softdropPuppiMass, 'FatJet1_softdropPuppiMass/F')
    FatJet1_softdropPuppiMassCorrBranch = newTree.Branch('FatJet1_softdropPuppiMassCorr', FatJet1_softdropPuppiMassCorr, 'FatJet1_softdropPuppiMassCorr/F')
    FatJet1_softdropPuppiMassCorrNotSmearedBranch = newTree.Branch('FatJet1_softdropPuppiMassCorrNotSmeared', FatJet1_softdropPuppiMassCorrNotSmeared, 'FatJet1_softdropPuppiMassCorrNotSmeared/F')
    FatJet1_puppiTau21Branch = newTree.Branch('FatJet1_puppiTau21', FatJet1_puppiTau21, 'FatJet1_puppiTau21/F')
    FatJet1_ddtTau21Branch = newTree.Branch('FatJet1_ddtTau21', FatJet1_ddtTau21, 'FatJet1_ddtTau21/F')
    FatJet1_CSVBranch = newTree.Branch('FatJet1_CSV', FatJet1_CSV, 'FatJet1_CSV/F')
    FatJet1_CSVRBranch = newTree.Branch('FatJet1_CSVR', FatJet1_CSVR, 'FatJet1_CSVR/F')
    FatJet1_CSV1Branch = newTree.Branch('FatJet1_CSV1', FatJet1_CSV1, 'FatJet1_CSV1/F')
    FatJet1_CSV2Branch = newTree.Branch('FatJet1_CSV2', FatJet1_CSV2, 'FatJet1_CSV2/F')
    FatJet1_CSVR1Branch = newTree.Branch('FatJet1_CSVR1', FatJet1_CSVR1, 'FatJet1_CSVR1/F')
    FatJet1_CSVR2Branch = newTree.Branch('FatJet1_CSVR2', FatJet1_CSVR2, 'FatJet1_CSVR2/F')
    V_massBranch = newTree.Branch('V_mass', V_mass, 'V_mass/F')
    V_ptBranch = newTree.Branch('V_pt', V_pt, 'V_pt/F')
    MEt_ptBranch = newTree.Branch('MEt_pt', MEt_pt, 'MEt_pt/F')
    X_massBranch = newTree.Branch('X_mass', X_mass, 'X_mass/F')    
    X_tmassBranch = newTree.Branch('X_tmass', X_tmass, 'X_tmass/F')    
    
    theweight = oldTree.GetWeight()
    
    for event in range(0, oldTree.GetEntries()-1):
        oldTree.GetEntry(event)

        # Alpha selections
        
        # Channel
        if not oldTree.isZtoMM and not oldTree.isZtoEE and not oldTree.isZtoNN: continue
        
        # Trigger
        if not oldTree.isMC:
            if oldTree.isZtoMM:
                #if not ( oldTree.HLT_TkMu50_v or oldTree.HLT_Mu50_v ): continue
                if not ( oldTree.HLT_Mu45_eta2p1_v ): continue
            elif oldTree.isZtoEE:
                if not ( oldTree.HLT_Ele105_CaloIdVT_GsfTrkIdT_v or oldTree.HLT_Ele115_CaloIdVT_GsfTrkIdT_v ): continue
            elif oldTree.isZtoNN:
                if not ( oldTree.HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v or oldTree.HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v or oldTree.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v or oldTree.HLT_PFMET170_NoiseCleaned_v or oldTree.HLT_PFMET170_JetIdCleaned_v or oldTree.HLT_PFMET170_HBHECleaned_v): continue
            else: continue
        # Leptons
        if oldTree.isZtoMM and not ( ((Lepton1.isHighPt and Lepton2.isHighPt) or (Lepton1.isTrackerHighPt and Lepton2.isHighPt) or (Lepton1.isHighPt and Lepton2.isTrackerHighPt)) and Lepton1.pt>55 and Lepton2.pt>20 and abs(Lepton1.eta)<2.1 and abs(Lepton2.eta)<2.1 and not (Lepton1.pt>500 and abs(Lepton1.eta)>1.2) and not (Lepton2.pt>500 and abs(Lepton2.eta)>1.2) and Lepton1.trkIso<0.1 and Lepton2.trkIso<0.1): continue

        if oldTree.isZtoEE and not (Lepton1.pt>135 and Lepton2.pt>35 and Lepton1.isLoose and Lepton2.isLoose): continue
        # No Leptons
        if oldTree.isZtoNN and not (MEt.pt>200 and oldTree.nLooseMuons==0 and oldTree.nVetoElectrons==0 and oldTree.nPhotons==0 and oldTree.nTaus==0 and oldTree.MinJetMetDPhi>0.5 and oldTree.Flag_EcalDeadCellTriggerPrimitiveFilter and oldTree.Flag_HBHENoiseFilter and oldTree.Flag_HBHENoiseIsoFilter and  oldTree.Flag_globalTightHalo2016Filter and oldTree.Flag_goodVertices and oldTree.Flag_BadPFMuon and oldTree.Flag_BadChCand): continue
        if not oldTree.isMC:
            if oldTree.isZtoNN and not oldTree.Flag_eeBadScFilter: continue
        # Boost and Z
        if (oldTree.isZtoEE or oldTree.isZtoMM) and not (V.pt>170 and FatJet1.pt>170 and V.mass>70 and V.mass<110): continue
        # Boost and Cleaning for Z invisible
        if oldTree.isZtoNN and not (FatJet1.pt>200 and FatJet1.isTight and FatJet1.nhf<0.8 and FatJet1.chf>0.2 and oldTree.MaxJetBTag<0.5426 and X.dPhi>2): continue
        # Grooming
        if not (FatJet1.softdropPuppiMassCorr>30): continue
        
        # Copy relevant variables
        EventNumber[0] = oldTree.EventNumber
        EventWeight[0] = oldTree.EventWeight * theweight
        RunNumber[0] = oldTree.RunNumber
        LumiNumber[0] = oldTree.LumiNumber
        isZtoEE[0] = oldTree.isZtoEE
        isZtoMM[0] = oldTree.isZtoMM
        isZtoNN[0] = oldTree.isZtoNN
        isMC[0] = oldTree.isMC
        FatJet1_pt[0] = FatJet1.pt
        FatJet1_softdropPuppiMass[0] = FatJet1.softdropPuppiMass
        FatJet1_softdropPuppiMassCorr[0] = FatJet1.softdropPuppiMassCorr
        FatJet1_softdropPuppiMassCorrNotSmeared[0] = FatJet1.softdropPuppiMassCorrNotSmeared
        FatJet1_puppiTau21[0] = FatJet1.puppiTau21
        FatJet1_ddtTau21[0] = FatJet1.ddtTau21
        FatJet1_CSV[0] = FatJet1.CSV
        FatJet1_CSVR[0] = FatJet1.CSVR
        FatJet1_CSV1[0] = FatJet1.CSV1
        FatJet1_CSV2[0] = FatJet1.CSV2
        FatJet1_CSVR1[0] = FatJet1.CSVR1
        FatJet1_CSVR2[0] = FatJet1.CSVR2
        V_mass[0] = V.mass
        V_pt[0] = V.pt
        MEt_pt[0] = MEt.pt
        X_mass[0] = X.mass
        X_tmass[0] = X.tmass
        
        newTree.Fill()
    
    print 'produced skimmed file',newFile.GetName(),'\tevents =',newTree.GetEntries(),'\tweight =',newTree.GetWeight()

    newFile.cd()
    newTree.Write()
    newFile.Close()
    oldFile.Close()
    

##########

subfiles = [x for x in os.listdir(args.folder) if os.path.isfile(os.path.join(args.folder, x))]

os.chdir(args.folder)

if not os.path.isdir('Skim'): os.mkdir('Skim')

for s in subfiles:
    #if 'Run2016' not in s: continue
#    print s
#    skim(s)
    p = multiprocessing.Process(target=skim, args=(s,))
    jobs.append(p)
    p.start()

#os.system('cd ..')

