#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from lcomp.lcomp import LCOMP
from lcomp.ldevioctl import (E440, L_STREAM_ADC, WDAQ_PAR,
                             L_ADC_PARAM, ASYNC_PAR, L_ASYNC_DAC_OUT,
                             L_ASYNC_ADC_INP, L_ASYNC_TTL_CFG, L_ASYNC_TTL_INP,
                             L_ASYNC_TTL_OUT, L_USER_BASE)
from lcomp.device import e440
from numpy import mean

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":

        with LCOMP(slot=0) as ldev:     # либо ldev.OpenLDevice() в начале и ldev.CloseLDevice() в конце
            print("LoadBios: {}".format(ldev.LoadBios("E440")))
            print("PlataTest: {}".format(ldev.PlataTest()))
            for i in range(20):
                print(i)
                slPar = ldev.GetSlotParam()
                print("GetSlotParam: {}".format(slPar))
                print("    Base:      {}".format(slPar.Base))
                print("    BaseL:     {}".format(slPar.BaseL))
                print("    Base1:     {}".format(slPar.Base1))
                print("    BaseL1:    {}".format(slPar.BaseL1))
                print("    Mem:       {}".format(slPar.Mem))
                print("    MemL:      {}".format(slPar.MemL))
                print("    Mem1:      {}".format(slPar.Mem1))
                print("    MemL1:     {}".format(slPar.MemL1))
                print("    Irq:       {}".format(slPar.Irq))
                print("    BoardType: {}".format(slPar.BoardType))
                print("    DSPType:   {}".format(slPar.DSPType))
                print("    Dma:       {}".format(slPar.Dma))
                print("    DmaDac:    {}".format(slPar.DmaDac))
                print("    DTA_REG:   {}".format(slPar.DTA_REG))
                print("    IDMA_REG:  {}".format(slPar.IDMA_REG))
                print("    CMD_REG:   {}".format(slPar.CMD_REG))
                print("    IRQ_RST:   {}".format(slPar.IRQ_RST))
                print("    DTA_ARRAY: {}".format(slPar.DTA_ARRAY))
                print("    RDY_REG:   {}".format(slPar.RDY_REG))
                print("    CFG_REG:   {}".format(slPar.CFG_REG))

                plDescr = ldev.ReadPlataDescr()
                print("ReadPlataDescr: {}".format(plDescr))

                # if slPar.BoardType == E440:
                #     print("    BrdName:      {}".format(plDescr.t4.BrdName))
                #     print("    SerNum:       {}".format(plDescr.t4.SerNum))
                #     print("    Rev:          {}".format(plDescr.t4.Rev))
                #     print("    DspType:      {}".format(plDescr.t4.DspType))
                #     print("    IsDacPresent: {}".format(bool(ord(plDescr.t4.IsDacPresent))))
                #     print("    Quartz:       {}".format(plDescr.t4.Quartz))
                #     print("    KoefADC:      {}".format(list(plDescr.t4.KoefADC)))
                #     print("    KoefDAC:      {}".format(list(plDescr.t4.KoefDAC)))

                # Потоковый вывод с АЦП

                buffer_size = ldev.RequestBufferStream(size=512, stream_id=L_STREAM_ADC)    # Желательно, чтобы размер буфера был
                print("RequestBufferStream: {}".format(buffer_size))                           # кратен числу используемых каналов NCh

                if slPar.BoardType == E440:
                    adcPar = WDAQ_PAR()

                    adcPar.t3.s_Type = L_ADC_PARAM
                    adcPar.t3.FIFO = 512
                    adcPar.t3.IrqStep = 512
                    adcPar.t3.Pages = 32
                    adcPar.t3.AutoInit = 0
                    adcPar.t3.dRate = 100
                    adcPar.t3.dKadr = 0.005
                    adcPar.t3.SynchroType = 0
                    adcPar.t3.SynchroSensitivity = 0
                    adcPar.t3.SynchroMode = 0
                    adcPar.t3.AdChannel = 0
                    adcPar.t3.AdPorog = 0
                    adcPar.t3.NCh = 8   # 2 # 3 # 4
                    # print(*adcPar.t3.Chn)
                    # adcPar.t3.Chn[4] = 0x4
                    adcPar.t3.Chn[0] = 0x0
                    adcPar.t3.Chn[1] = 0x1
                    adcPar.t3.Chn[2] = 0x2
                    adcPar.t3.Chn[3] = 0x3
                    adcPar.t3.Chn[4] = 0x4
                    adcPar.t3.Chn[5] = 0x5
                    adcPar.t3.Chn[6] = 0x6
                    adcPar.t3.Chn[7] = 0x7
                    # print(*adcPar.t3.Chn)
                    adcPar.t3.IrqEna = 1
                    adcPar.t3.AdcEna = 1

                    print("FillDAQparameters: {}".format(ldev.FillDAQparameters(adcPar.t3)))
                    print("    s_Type:             {}".format(adcPar.t3.s_Type))
                    print("    FIFO:               {}".format(adcPar.t3.FIFO))
                    print("    IrqStep:            {}".format(adcPar.t3.IrqStep))
                    print("    Pages:              {}".format(adcPar.t3.Pages))
                    print("    AutoInit:           {}".format(adcPar.t3.AutoInit))
                    print("    dRate:              {}".format(adcPar.t3.dRate))
                    print("    dKadr:              {}".format(adcPar.t3.dKadr))
                    print("    dScale:             {}".format(adcPar.t3.dScale))
                    print("    Rate:               {}".format(adcPar.t3.Rate))
                    print("    Kadr:               {}".format(adcPar.t3.Kadr))
                    print("    Scale:              {}".format(adcPar.t3.Scale))
                    print("    FPDelay:            {}".format(adcPar.t3.FPDelay))
                    print("    SynchroType:        {}".format(adcPar.t3.SynchroType))
                    print("    SynchroSensitivity: {}".format(adcPar.t3.SynchroSensitivity))
                    print("    SynchroMode:        {}".format(adcPar.t3.SynchroMode))
                    print("    AdChannel:          {}".format(adcPar.t3.AdChannel))
                    print("    AdPorog:            {}".format(adcPar.t3.AdPorog))
                    print("    NCh:                {}".format(adcPar.t3.NCh))
                    # print("    Chn:                {}".format(list(adcPar.t3.Chn)))
                    print("    IrqEna:             {}".format(adcPar.t3.IrqEna))
                    print("    AdcEna:             {}".format(adcPar.t3.AdcEna))

                    data_ptr, syncd = ldev.SetParametersStream(adcPar.t3, buffer_size)
                    print("SetParametersStream: {}, {}".format(data_ptr, syncd))
                    print("    Pages:   {}".format(adcPar.t3.Pages))
                    print("    IrqStep: {}".format(adcPar.t3.IrqStep))
                    print("    FIFO:    {}".format(adcPar.t3.FIFO))
                    print("    Rate:    {}".format(adcPar.t3.dRate))

                print("EnableCorrection: {}".format(ldev.EnableCorrection(True)))

                print("InitStartLDevice: {}".format(ldev.InitStartLDevice()))
                print("StartLDevice: {}".format(ldev.StartLDevice()))

                # print("Read data from buffer ...")



                while syncd() < buffer_size:            # ждем, пока заполнится буфер
                    pass

                print("Data ready ...")

                if slPar.BoardType == E440:
                    x = e440.GetDataADC(adcPar.t3, plDescr, data_ptr, buffer_size)


                with open("channel-1.log", 'a') as fh:
                    for j in x:
                        fh.write(str(mean(j).tolist()) + ' ')        # индекс соответствует номеру канала из Chn
                    fh.write('\n')
                print(syncd)
                del syncd
                data_ptr, syncd = ldev.SetParametersStream(adcPar.t3, buffer_size)
                print(syncd)
                # with open("channel-2.log", 'w') as fh:
                #     fh.write(str(x[1].tolist()))
                # with open("channel-3.log", 'w') as fh:
                #     fh.write(str(x[2].tolist()))

                print("StopLDevice: {}".format(ldev.StopLDevice()))

                # Асинхронные операции ввода/вывода

                # asp = ASYNC_PAR()
                #
                # asp.s_Type = L_ASYNC_DAC_OUT
                # asp.Mode = 0
                # asp.Data[0] = 512
                # if ldev.IoAsync(asp):
                #     print("IoAsync (L_ASYNC_DAC_OUT): {}".format(asp.Data[0]))
                #
                # asp.s_Type = L_ASYNC_ADC_INP
                # asp.Chn[0] = 0x00
                # if ldev.IoAsync(asp):
                #     print("IoAsync (L_ASYNC_ADC_INP): {}".format(asp.Data[0]))
                #
                # asp.s_Type = L_ASYNC_TTL_CFG
                # asp.Mode = 1
                # if ldev.IoAsync(asp):
                #     print("IoAsync (L_ASYNC_TTL_CFG): {}".format(asp.Data[0]))
                #
                # asp.s_Type = L_ASYNC_TTL_INP
                # asp.Chn[0] = 0x00
                # if ldev.IoAsync(asp):
                #     print("IoAsync (L_ASYNC_TTL_INP): {}".format(asp.Data[0]))

                # asp.s_Type = L_ASYNC_TTL_OUT
                # asp.Data[0] = 0xA525
                # if ldev.IoAsync(asp):
                #     print("IoAsync (L_ASYNC_TTL_OUT): {}".format(asp.Data[0]))
                #
                # Проверка работоспособности других функций

                # print("SetParameter (L_USER_BASE): {}".format(ldev.SetParameter(name=L_USER_BASE, value=123)))
                # print("GetParameter (L_USER_BASE): {}".format(ldev.GetParameter(name=L_USER_BASE)))
                # print("ReadFlashWord: {}".format(ldev.ReadFlashWord(address=L_USER_BASE)))
                # print("EnableFlashWrite: {}".format(ldev.EnableFlashWrite(False)))
                # print("SendCommand: {}".format(ldev.SendCommand(cmd=0)))
                # print("SetLDeviceEvent: {}".format(ldev.SetLDeviceEvent(event=0, event_id=L_STREAM_ADC)))
                #
                # print("GetWord_DM: {}".format(ldev.GetWord_DM(address=0x0400)))
                # print("GetWord_PM: {}".format(ldev.GetWord_PM(address=0)))
                # print("GetArray_DM: {}".format(ldev.GetArray_DM(address=0x1080, count=2)))
                # print("GetArray_PM: {}".format(ldev.GetArray_PM(address=0, count=2)))

                # print("inbyte: {}".format(ldev.inbyte(offset=0x1080)))
                # print("inword: {}".format(ldev.inword(offset=0x1080)))
                # print("indword: {}".format(ldev.indword(offset=0x1080)))
                # print("inmbyte: {}".format(ldev.inmbyte(offset=0x1080)))
                # print("inmword: {}".format(ldev.inmword(offset=0x1080)))
                # print("inmdword: {}".format(ldev.inmdword(offset=0x1080)))
