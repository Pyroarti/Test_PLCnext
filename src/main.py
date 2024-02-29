from PyPlcnextRsc import Device, GUISupplierExample, ConsoleSupplierExample
from PyPlcnextRsc.Arp.Plc.Gds.Services import IDataAccessService, ISubscriptionService, IForceService
from PyPlcnextRsc.Arp.Device.Interface.Services import IDeviceInfoService, IDeviceStatusService


with Device('192.168.11.198',  secureInfoSupplier=ConsoleSupplierExample) as device:
    service1 = IDataAccessService(device)
    service2 = ISubscriptionService(device)
    service3 = IForceService(device)

    service4 = IDeviceInfoService(device)

    print(service1)
    print(service2)
    print(service3)
    print(service4)

    device_info_service = IDeviceInfoService(device)
    device_status_service = IDeviceStatusService(device)
    info_items = [
        "General.ArticleName",
        "General.ArticleNumber",
        "General.SerialNumber",
        "General.Firmware.Version",
        "General.Hardware.Version",
        "Interfaces.Ethernet.1.0.Mac"
    ]
    status_items = [
        "Status.Cpu.0.Load.Percent",
        "Status.Memory.Usage.Percent",
        "Status.ProgramMemoryIEC.Usage.Percent",
        "Status.DataMemoryIEC.Usage.Percent",
        "Status.Board.Temperature.Centigrade",
        "Status.Board.Temperature.Centigrade",
        "Status.Board.Humidity"
    ]
    for identifier, result in zip(info_items, device_info_service.GetItems(info_items)):
        print(identifier.rjust(40) + " : " + str(result.GetValue()))
    for identifier, result in zip(status_items, device_status_service.GetItems(status_items)):
        print(identifier.rjust(40) + " : " + str(result.GetValue()))
