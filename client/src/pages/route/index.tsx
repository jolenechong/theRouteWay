import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import Form from '../../components/form';
import RoutesBox from '../../components/routesBox';

function GetRoute() {

    const [searchParams, setSearchParams] = useSearchParams();
    const [route, routes] = useState([]);
    // TODO: initialise routes from algo here, use useeffect

    const source = searchParams.get('source') as string;
    const destination = searchParams.get('destination') as string;

  return (
    <>
        <>
        <div className='tw-flex tw-justify-center tw-p-10'>
        <div className='tw-flex-1'>
        <Form source={source} destination={destination}/>
        </div>
        <div className='tw-flex-1 tw-pl-10'>
            <h1>Retrieveing Your Best Routes...</h1>
            {/* only load this part after submitting form and when it returns data */}
            {/* do mapping frm a list and use this component a few times */}
            <RoutesBox option={0} timeStart={'6.43pm'} timeEnd={'7.26pm'} destination={destination} source={source} timeNeeded={40} delay={false} route={[]} />
            <RoutesBox option={0} timeStart={'6.43pm'} timeEnd={'7.26pm'} destination={destination} source={source} timeNeeded={40} delay={true} delayTime={5} route={[]}/>
        </div>
        </div>
        </>
    </>
  );
}

export default GetRoute;