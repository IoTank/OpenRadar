import serial
import time
import os
import json
import keyboard

# prerequest
# Evm use out of box demo
# i18xwr flash out of demo
# S1 switch to 001


# 1. config file
# configFileName = 'C:/Users/Zber/Desktop/mmWave Configuration/tx3_rx4_bestRange_beamforming_3region.cfg'
configFileName = r'C:/ti/mmwave_studio_02_01_01_00/mmWaveStudio/PostProc/profile_3d_aop_3s.cfg'

# 2. datacard_config move to mmWave studio folder (postproc)
datacard_config = 'C:/ti/mmwave_studio_02_01_01_00/mmWaveStudio/PostProc/datacard_config.json'

# 3. postproc path under mmwave studio folder
postproc_path = "C:/ti/mmwave_studio_02_01_01_00/mmWaveStudio/PostProc"

# 4. CLI port , Dataport COMXX confirm


CLIport = {}
Dataport = {}
real_time = False


# ------------------------------------------------------------------

# Function to configure the serial ports and send the data from
# the configuration file to the radar
def serialConfig(configFileName):
    global CLIport
    global Dataport
    # Open the serial ports for the configuration and the data ports

    # Raspberry pi
    # CLIport = serial.Serial('/dev/ttyACM0', 115200)
    # Dataport = serial.Serial('/dev/ttyACM1', 921600)

    # Windows
    CLIport = serial.Serial('COM23', 115200)
    Dataport = serial.Serial('COM22', 921600)

    # Read the configuration file and send it to the board
    config = [line.rstrip('\r\n') for line in open(configFileName)]
    for i in config:
        CLIport.write((i + '\n').encode())
        print(i)
        time.sleep(0.001)
    # CLIport.close()  #关闭串口，使用不到该命令
    # Dataport.close()
    return CLIport, Dataport


def send_stop():
    global CLIport
    global Dataport
    # Open the serial ports for the configuration and the data ports

    # Raspberry pi
    # CLIport = serial.Serial('/dev/ttyACM0', 115200)
    # Dataport = serial.Serial('/dev/ttyACM1', 921600)

    # Windows
    CLIport = serial.Serial('COM23', 115200)
    Dataport = serial.Serial('COM22', 921600)

    CLIport.write(('sensorStop' + '\n').encode())
    print("Sensor Stopped!")

    CLIport.close()
    Dataport.close()


# ------------------------------------------------------------------

# Function to parse the data inside the configuration file
# def parseConfigFile(configFileName):
#     configParameters = {}  # Initialize an empty dictionary to store the configuration parameters
#
#     # Read the configuration file and send it to the board
#     config = [line.rstrip('\r\n') for line in open(configFileName)]
#     for i in config:
#
#         # Split the line
#         splitWords = i.split(" ")
#
#         # Hard code the number of antennas, change if other configuration is used
#         numRxAnt = 4
#         numTxAnt = 3
#
#         # Get the information about the profile configuration
#         if "profileCfg" in splitWords[0]:
#             startFreq = int(float(splitWords[2]))
#             idleTime = int(splitWords[3])
#             rampEndTime = float(splitWords[5])
#             freqSlopeConst = float(splitWords[8])
#             numAdcSamples = int(splitWords[10])
#             numAdcSamplesRoundTo2 = 1
#
#             while numAdcSamples > numAdcSamplesRoundTo2:
#                 numAdcSamplesRoundTo2 = numAdcSamplesRoundTo2 * 2
#
#             digOutSampleRate = int(splitWords[11])
#
#         # Get the information about the frame configuration
#         elif "frameCfg" in splitWords[0]:
#
#             chirpStartIdx = int(splitWords[1])
#             chirpEndIdx = int(splitWords[2])
#             numLoops = int(splitWords[3])
#             numFrames = int(splitWords[4])
#             configParameters['numFrames'] = numFrames
#             framePeriodicity = float(splitWords[5])
#
#     # Combine the read data to obtain the configuration parameters
#     numChirpsPerFrame = (chirpEndIdx - chirpStartIdx + 1) * numLoops
#     configParameters["numDopplerBins"] = numChirpsPerFrame / numTxAnt
#     configParameters["numRangeBins"] = numAdcSamplesRoundTo2
#     configParameters["rangeResolutionMeters"] = (3e8 * digOutSampleRate * 1e3) / (
#             2 * freqSlopeConst * 1e12 * numAdcSamples)
#     configParameters["rangeIdxToMeters"] = (3e8 * digOutSampleRate * 1e3) / (
#             2 * freqSlopeConst * 1e12 * configParameters["numRangeBins"])
#     configParameters["dopplerResolutionMps"] = 3e8 / (
#             2 * startFreq * 1e9 * (idleTime + rampEndTime) * 1e-6 * configParameters["numDopplerBins"] * numTxAnt)
#     configParameters["maxRange"] = (300 * 0.9 * digOutSampleRate) / (2 * freqSlopeConst * 1e3)
#     configParameters["maxVelocity"] = 3e8 / (4 * startFreq * 1e9 * (idleTime + rampEndTime) * 1e-6 * numTxAnt)
#
#     return configParameters


# ------------------------------------------------------------------
# # Funtion to read and parse the incoming data
# def readAndParseData18xx(Dataport, configParameters):
#     global byteBuffer, byteBufferLength
#
#     # Constants
#     OBJ_STRUCT_SIZE_BYTES = 12;
#     BYTE_VEC_ACC_MAX_SIZE = 2 ** 15;
#     MMWDEMO_UART_MSG_DETECTED_POINTS = 1;
#     MMWDEMO_UART_MSG_RANGE_PROFILE = 2;
#     maxBufferSize = 2 ** 15;
#     tlvHeaderLengthInBytes = 8;
#     pointLengthInBytes = 16;
#     magicWord = [2, 1, 4, 3, 6, 5, 8, 7]
#
#     # Initialize variables
#     magicOK = 0  # Checks if magic number has been read
#     dataOK = 0  # Checks if the data has been read correctly
#     frameNumber = 0
#     detObj = {}
#
#     readBuffer = Dataport.read(Dataport.in_waiting)
#     byteVec = np.frombuffer(readBuffer, dtype='uint8')
#     byteCount = len(byteVec)
#
#     # Check that the buffer is not full, and then add the data to the buffer
#     if (byteBufferLength + byteCount) < maxBufferSize:
#         byteBuffer[byteBufferLength:byteBufferLength + byteCount] = byteVec[:byteCount]
#         byteBufferLength = byteBufferLength + byteCount
#
#     # Check that the buffer has some data
#     if byteBufferLength > 16:
#
#         # Check for all possible locations of the magic word
#         possibleLocs = np.where(byteBuffer == magicWord[0])[0]
#
#         # Confirm that is the beginning of the magic word and store the index in startIdx
#         startIdx = []
#         for loc in possibleLocs:
#             check = byteBuffer[loc:loc + 8]
#             if np.all(check == magicWord):
#                 startIdx.append(loc)
#
#         # Check that startIdx is not empty
#         if startIdx:
#
#             # Remove the data before the first start index
#             if startIdx[0] > 0 and startIdx[0] < byteBufferLength:
#                 byteBuffer[:byteBufferLength - startIdx[0]] = byteBuffer[startIdx[0]:byteBufferLength]
#                 byteBuffer[byteBufferLength - startIdx[0]:] = np.zeros(len(byteBuffer[byteBufferLength - startIdx[0]:]),
#                                                                        dtype='uint8')
#                 byteBufferLength = byteBufferLength - startIdx[0]
#
#             # Check that there have no errors with the byte buffer length
#             if byteBufferLength < 0:
#                 byteBufferLength = 0
#
#             # word array to convert 4 bytes to a 32 bit number
#             word = [1, 2 ** 8, 2 ** 16, 2 ** 24]
#
#             # Read the total packet length
#             totalPacketLen = np.matmul(byteBuffer[12:12 + 4], word)
#
#             # Check that all the packet has been read
#             if (byteBufferLength >= totalPacketLen) and (byteBufferLength != 0):
#                 magicOK = 1
#
#     # If magicOK is equal to 1 then process the message
#     if magicOK:
#         # word array to convert 4 bytes to a 32 bit number
#         word = [1, 2 ** 8, 2 ** 16, 2 ** 24]
#
#         # Initialize the pointer index
#         idX = 0
#
#         # Read the header
#         magicNumber = byteBuffer[idX:idX + 8]
#         idX += 8
#         version = format(np.matmul(byteBuffer[idX:idX + 4], word), 'x')
#         idX += 4
#         totalPacketLen = np.matmul(byteBuffer[idX:idX + 4], word)
#         idX += 4
#         platform = format(np.matmul(byteBuffer[idX:idX + 4], word), 'x')
#         idX += 4
#         frameNumber = np.matmul(byteBuffer[idX:idX + 4], word)
#         idX += 4
#         timeCpuCycles = np.matmul(byteBuffer[idX:idX + 4], word)
#         idX += 4
#         numDetectedObj = np.matmul(byteBuffer[idX:idX + 4], word)
#         idX += 4
#         numTLVs = np.matmul(byteBuffer[idX:idX + 4], word)
#         idX += 4
#         subFrameNumber = np.matmul(byteBuffer[idX:idX + 4], word)
#         idX += 4
#
#         # Read the TLV messages
#         for tlvIdx in range(numTLVs):
#
#             # word array to convert 4 bytes to a 32 bit number
#             word = [1, 2 ** 8, 2 ** 16, 2 ** 24]
#
#             # Check the header of the TLV message
#             tlv_type = np.matmul(byteBuffer[idX:idX + 4], word)
#             idX += 4
#             tlv_length = np.matmul(byteBuffer[idX:idX + 4], word)
#             idX += 4
#
#             # Read the data depending on the TLV message
#             if tlv_type == MMWDEMO_UART_MSG_DETECTED_POINTS:
#
#                 # Initialize the arrays
#                 x = np.zeros(numDetectedObj, dtype=np.float32)
#                 y = np.zeros(numDetectedObj, dtype=np.float32)
#                 z = np.zeros(numDetectedObj, dtype=np.float32)
#                 velocity = np.zeros(numDetectedObj, dtype=np.float32)
#
#                 for objectNum in range(numDetectedObj):
#                     # Read the data for each object
#                     x[objectNum] = byteBuffer[idX:idX + 4].view(dtype=np.float32)
#                     idX += 4
#                     y[objectNum] = byteBuffer[idX:idX + 4].view(dtype=np.float32)
#                     idX += 4
#                     z[objectNum] = byteBuffer[idX:idX + 4].view(dtype=np.float32)
#                     idX += 4
#                     velocity[objectNum] = byteBuffer[idX:idX + 4].view(dtype=np.float32)
#                     idX += 4
#
#                 # Store the data in the detObj dictionary
#                 detObj = {"numObj": numDetectedObj, "x": x, "y": y, "z": z, "velocity": velocity}
#                 dataOK = 1
#
#         # Remove already processed data
#         if idX > 0 and byteBufferLength > idX:
#             shiftSize = totalPacketLen
#
#             byteBuffer[:byteBufferLength - shiftSize] = byteBuffer[shiftSize:byteBufferLength]
#             byteBuffer[byteBufferLength - shiftSize:] = np.zeros(len(byteBuffer[byteBufferLength - shiftSize:]),
#                                                                  dtype='uint8')
#             byteBufferLength = byteBufferLength - shiftSize
#
#             # Check that there are no errors with the buffer length
#             if byteBufferLength < 0:
#                 byteBufferLength = 0
#
#     return dataOK, frameNumber, detObj


# ------------------------------------------------------------------

# Funtion to update the data and display in the plot

# def update():
#     dataOk = 0
#     global detObj
#     x = []
#     y = []
#
#     # Read and parse the received data
#     dataOk, frameNumber, detObj = readAndParseData18xx(Dataport, configParameters)
#
#     if dataOk and len(detObj["x"]) > 0:
#         # print(detObj)
#         x = -detObj["x"]
#         y = detObj["y"]
#
#         # s.setData(x, y)
#         # QtGui.QApplication.processEvents()
#
#     return dataOk


def update_data_config(jsonfile, file_prefix, file_basepath):
    with open(jsonfile, 'r+') as f:
        data = json.load(f)
        data['DCA1000Config']['captureConfig']['fileBasePath'] = file_basepath
        data['DCA1000Config']['captureConfig']['filePrefix'] = file_prefix

        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part

    time.sleep(0.05)


# Function to
def send_cli():
    # import subprocess

    json_file_name = "datacard_config.json"
    cwd = os.getcwd()
    os.chdir(postproc_path)
    # os.system(f"DCA1000EVM_CLI_Control.exe reset_fpga {json_file_name}")
    os.system(f"DCA1000EVM_CLI_Control.exe fpga {json_file_name}")
    os.system(f"DCA1000EVM_CLI_Control.exe record {json_file_name}")
    os.system(f"DCA1000EVM_CLI_Control.exe start_record {json_file_name}")
    CLIport, Dataport = serialConfig(configFileName)

    # real time, terminate manually
    if real_time:
        print("real-time data collecting, press Esc to exit: ")
        while True:
            try:
                if keyboard.is_pressed('Esc'):
                    print("you pressed Esc, quit data collection..")
                    os.system(f"DCA1000EVM_CLI_Control.exe stop_record {json_file_name}")
                    os.chdir(cwd)
                    time.sleep(1)
                    send_stop()
                    break
            except:
                break
    # os.system(f"DCA1000EVM_CLI_Control.exe stop_record {json_file_name}")
    # os.chdir(cwd)

    return CLIport, Dataport


# Get the configuration parameters from the configuration file
# configParameters = parseConfigFile(configFileName)

# -------------------------    MAIN   -----------------------------------------

if __name__ == "__main__":
    start_index = 0
    end_index = 1
    file_name = "Running_{}"
    file_basepath = r"E:\labotory\mmwave\project\OpenRadar\SavedData"

    # interval time >> capture time e.g. ct=5 , interval=8
    interval_time = 10

    # send_stop()
    for i in range(start_index, end_index):

        # preparing data config json file
        file_prefix = file_name.format(i)
        update_data_config(datacard_config, file_prefix, file_basepath)

        # preparing data capture
        # time_start = time.time()
        CLIport, Dataport = send_cli()

        time.sleep(interval_time)

        # close data port
        CLIport.write(('sensorStop\n').encode())
        print("Sensor stops")
        CLIport.close()
        Dataport.close()