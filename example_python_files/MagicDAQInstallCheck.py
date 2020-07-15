# This script checks that the MagicDAQ API and MagicDAQ Driver were installed properly
# It is NOT NECESSARY to have the MagiDAQ connected to the computer

print('*** MagicDAQ Install Check***')
print('')

try:

    # Import MagicDAQDevice object
    from magicdaq.api_class import MagicDAQDevice

    # Create daq_one object
    daq_one = MagicDAQDevice()
    print('GOOD: MagicDAQ API is installed properly.')

    # Get MagicDAQ Driver Version
    driver_version = daq_one.get_driver_version()

    if driver_version == 1.0:
        print('GOOD: MagicDAQ Driver is installed properly.')
        print('You are ready to use MagicDAQ!')
    else:
        print('ERROR: MagicDAQ Driver version not expected value: '+str(driver_version))
        print('Try installing MagicDAQ using pip again.')
        print('https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ')
        print('Feel free to email MagicDAQ Support at: support@magicdaq.com')

except Exception as exception_text:
    print('Original exception: ')
    print(exception_text)
    print('')
    print('ERROR: Unable to import MagicDAQ API.')
    print('Mostly likely, MagicDAQ has not been properly downloaded and installed using pip.')
    print('Please consult MagicDAQ API Docs: https://magicdaq.github.io/magicdaq_docs/#/Install_MagicDAQ')
    print('Feel free to email MagicDAQ Support at: support@magicdaq.com')

print('')
print('*** MagicDAQ Install Check Completed***')
