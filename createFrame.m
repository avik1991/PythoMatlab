function Status = createFrame(alV,Tx_time,BW,Mcs,data)
    allocationIndex = alV; 
    cfgMU = wlanHEMUConfig(allocationIndex);
    figure;
    hePlotAllocation(cfgMU);
    axAlloc = gca;
    allocationInfo = ruInfo(cfgMU);

    disp(class(data))

    numUsers = allocationInfo.NumUsers;
    cfgTriggerUser = repmat({heTBConfig},1,numUsers);
    cfgMU.TXOPDuration=Tx_time;


    trigInd = heTBFieldIndices(cfgTriggerUser{1}); % Get the indices of each field
    txTrigStore = zeros(trigInd.HEData(2),numUsers);
    for userIdx = 1:numUsers
        % Generate waveform for a user
        cfgTrigger = cfgTriggerUser{userIdx};
        %txPSDU = randi([0 1],getPSDULength(cfgTrigger)*8,1);
        dataPart=randi([0 0],data{userIdx},1);
        padPart=randi([1 1],(getPSDULength(cfgTrigger)*8)-data{userIdx},1);
        %txTrig = heTBWaveformGenerator(txPSDU,cfgTrigger);
        txTrig = heTBWaveformGenerator(cat(1,dataPart,padPart),cfgTrigger);
        % Store the transmitted STA waveform for analysis
        txTrigStore(:,userIdx) = sum(txTrig,2);
    end

    spectrumAnalyzer = dsp.SpectrumAnalyzer;
    spectrumAnalyzer.SampleRate = heTBSampleRate(cfgTriggerUser{1});
    spectrumAnalyzer.ChannelNames = {'RU#1 User 1','RU#1 User 2','RU#2'};
    spectrumAnalyzer.ShowLegend = true;
    spectrumAnalyzer.Title = 'Transmitted HE-TB Waveform per User';
    spectrumAnalyzer(txTrigStore);   
 
    Status =txTrigStore ;


end