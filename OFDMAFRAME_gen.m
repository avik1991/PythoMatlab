% Generate an OFDMA allocation
cfgMU = wlanHEMUConfig(97);
allocationInfo = ruInfo(cfgMU);

% These parameters are the same for all users in the OFDMA system
channelBandwidth = cfgMU.ChannelBandwidth; % Bandwidth of OFDMA system
numSymbols = 20;          % Number of HE data field symbols
preFECPaddingFactor = 2;  % Pre-FEC padding factor
ldpcExtraSymbol = false;  % LDPC extra symbol
numHELTFSymbols = 2;      % Number of HE-LTF symbols

% Create a trigger configuration for each user
numUsers = allocationInfo.NumUsers;
cfgTriggerUser = repmat({heTBConfig},1,numUsers);

for userIdx = 1:numUsers
    cfgTriggerUser{userIdx}.ChannelBandwidth = channelBandwidth;
    cfgTriggerUser{userIdx}.NumDataSymbols = numSymbols;
    cfgTriggerUser{userIdx}.PreFECPaddingFactor = preFECPaddingFactor;
    cfgTriggerUser{userIdx}.LDPCExtraSymbol = ldpcExtraSymbol;
    cfgTriggerUser{userIdx}.NumHELTFSymbols = numHELTFSymbols;
    cfgTriggerUser{userIdx}.TXOPDuration = 127;

end


% These parameters are for the first user - RU#1 MU-MIMO user 1
cfgTriggerUser{1}.RUSize = allocationInfo.RUSizes(1);
cfgTriggerUser{1}.RUIndex = allocationInfo.RUIndices(1);
cfgTriggerUser{1}.MCS = 4;                     % Modulation and coding scheme
cfgTriggerUser{1}.NumSpaceTimeStreams = 1;     % Number of space-time streams
cfgTriggerUser{1}.NumTransmitAntennas = 1;     % Number of transmit antennas
cfgTriggerUser{1}.StartingSpaceTimeStream = 1; % The starting index of the space-time streams
cfgTriggerUser{1}.ChannelCoding = 'LDPC';      % Channel coding

% These parameters are for the second user - RU#1 MU-MIMO user 2
cfgTriggerUser{2}.RUSize = allocationInfo.RUSizes(1);
cfgTriggerUser{2}.RUIndex = allocationInfo.RUIndices(1);
cfgTriggerUser{2}.MCS = 3;                     % Modulation and coding scheme
cfgTriggerUser{2}.NumSpaceTimeStreams = 1;     % Number of space-time streams
cfgTriggerUser{2}.StartingSpaceTimeStream = 2; % The starting index of the space-time streams
cfgTriggerUser{2}.NumTransmitAntennas = 1;     % Number of transmit antennas
cfgTriggerUser{2}.ChannelCoding = 'LDPC';      % Channel coding

% These parameters are for the third user - RU#2
cfgTriggerUser{3}.RUSize = allocationInfo.RUSizes(2);
cfgTriggerUser{3}.RUIndex = allocationInfo.RUIndices(2);
cfgTriggerUser{3}.MCS = 4;                     % Modulation and coding scheme
cfgTriggerUser{3}.NumSpaceTimeStreams = 2;     % Number of space-time streams
cfgTriggerUser{3}.StartingSpaceTimeStream = 1; % The starting index of the space-time streams
cfgTriggerUser{3}.NumTransmitAntennas = 2;     % Number of transmit antennas
cfgTriggerUser{3}.ChannelCoding = 'BCC';       % Channel coding


trigInd = heTBFieldIndices(cfgTriggerUser{1}); % Get the indices of each field
txTrigStore = zeros(trigInd.HEData(2),numUsers);
for userIdx = 1:numUsers
    % Generate waveform for a user
    cfgTrigger = cfgTriggerUser{userIdx};
    txPSDU = randi([0 1],getPSDULength(cfgTrigger)*8,1);
    txTrig = heTBWaveformGenerator(txPSDU,cfgTrigger);

    % Store the transmitted STA waveform for analysis
    txTrigStore(:,userIdx) = sum(txTrig,2);
end

spectrumAnalyzer = dsp.SpectrumAnalyzer;
spectrumAnalyzer.SampleRate = heTBSampleRate(cfgTriggerUser{1});
spectrumAnalyzer.ChannelNames = {'RU#1 User 1','RU#1 User 2','RU#2'};
spectrumAnalyzer.ShowLegend = true;
spectrumAnalyzer.Title = 'Transmitted HE-TB Waveform per User';
spectrumAnalyzer(txTrigStore);