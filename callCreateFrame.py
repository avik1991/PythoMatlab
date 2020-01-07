import matlab.engine

def GetAllocationIndex(ruAllocArray):
    allocationIndexStr="";
    if len(ruAllocArray)==9:
        allocationIndexStr="00000000"
    elif len(ruAllocArray)==8:
        if ruAllocArray[8]==2:
            allocationIndexStr="00000001"
        elif ruAllocArray[0]==2:
            allocationIndexStr="00001000"
        elif ruAllocArray[5]==2:
            allocationIndexStr="00000010"
        elif ruAllocArray[2]==2:
            allocationIndexStr="00000100"
    elif len(ruAllocArray)==7:
        if ruAllocArray[6]==2 and ruAllocArray[5]==2:
            allocationIndexStr="00000011"
        elif ruAllocArray[6]==2 and ruAllocArray[2]==2:
            allocationIndexStr="00000101"
        elif ruAllocArray[2]==2 and ruAllocArray[4]==2:
            allocationIndexStr="00000110"
        elif ruAllocArray[6]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001001"
        elif ruAllocArray[0]==2 and ruAllocArray[4]==2:
            allocationIndexStr="00001010"
        elif ruAllocArray[0]==2 and ruAllocArray[1]==2:
            allocationIndexStr="00001100"
    elif len(ruAllocArray)==6:
        if ruAllocArray[5]==2 and ruAllocArray[4]==2 and ruAllocArray[2]==2:
            allocationIndexStr="00000111"
        elif ruAllocArray[5]==2 and ruAllocArray[4]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001011"
        elif ruAllocArray[5]==2 and ruAllocArray[1]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001101"
        elif ruAllocArray[3]==2 and ruAllocArray[1]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001110"
    elif len(ruAllocArray)==5:
        if ruAllocArray[2]==1 and ruAllocArray[0]==2 and ruAllocArray[4]==2:
            allocationIndexStr="00001111"
    return allocationIndexStr;

def createMatlabFrame(ruVec_,Tx_t_,BW_,mcs_,data_):
    eng = matlab.engine.start_matlab()
    tf = eng.createFrame(GetAllocationIndex(ruVec_),Tx_t_,BW_,mcs_,data_)
    print(tf)
    return tf;

tx_signal=createMatlabFrame([2,1,1,1,2,2],127,'CBW20',3,[500,500,500,600,600,800])

