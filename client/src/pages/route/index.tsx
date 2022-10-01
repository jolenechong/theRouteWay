import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import Form from '../../components/form';
import RoutesBox from '../../components/routesBox';
// @ts-ignore
import map from '../../data/map.png';
// @ts-ignore
import road1n2 from '../../data/roads/Road 1 and 2.png';

function GetRoute() {

    const [searchParams, setSearchParams] = useSearchParams();
    const [route, routes] = useState([]);
    const [displayDir, setDisplayDir] = useState(false);

    // TODO: initialise routes from algo here, use useeffect

    const source = searchParams.get('source') as string;
    const destination = searchParams.get('destination') as string;

  return (
    <>
        <>
        { !displayDir ? 
        // if dw display yet den show all results
        <div className='tw-flex tw-justify-center tw-p-10'>
        <div className='tw-flex-1'>
        <Form source={source} destination={destination}/>
        </div>
        <div className='tw-flex-1 tw-pl-10'>
            <h1>Retrieveing Your Best Routes...</h1>
            {/* only load this part after submitting form and when it returns data */}
            {/* do mapping frm a list and use this component a few times */}
            <RoutesBox option={0} timeStart={'6.43pm'} timeEnd={'7.26pm'} destination={destination} source={source} timeNeeded={40} delay={false} route={[]} setDisplayDir={setDisplayDir}/>
            <RoutesBox option={0} timeStart={'6.43pm'} timeEnd={'7.26pm'} destination={destination} source={source} timeNeeded={40} delay={true} delayTime={5} route={[]} setDisplayDir={setDisplayDir}/>
        </div>
        </div>
        :
        // display one result map view
        <div className='tw-flex tw-h-screen tw-w-screen'>
        <div className="tw-shadow tw-p-4 tw-w-[20%]">
            <h1 className="tw-pt-8">Map View</h1>
            <p>From {source} to {destination}.</p>
            <p className='tw-font-bold tw-text-xl'>Option {0}</p>
            <p className='tw-font-bold tw-text-lg'>{0}: {0}</p>
            <p className='tw-font-bold tw-text-lg'>Roads to Pass:</p>
            {route.map((road, index) => {
                return <p key={index}>{road}</p>
            })}


        </div>
        <div className='tw-shadow tw-w-[80%]'>
          <div className='tw-relative tw-w-full tw-h-screen'>
            <img src={map} alt='map' className='tw-h-screen tw-w-full tw-overflow-scroll tw-absolute tw-top-0 tw-right-0'/>
            <img src={road1n2} alt='map' className='tw-h-screen tw-w-full tw-overflow-scroll tw-absolute tw-top-0 tw-right-0'/>
          </div>
        </div>
    </div>}
        </>
    </>
  );
}

export default GetRoute;