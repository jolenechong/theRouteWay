import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import Form from '../../components/form';
import RoutesBox, { RouteDetails } from '../../components/routesBox';
// @ts-ignore
import map from '../../data/map.png';

interface Object {
  [key: string]: string;
}

function GetRoute() {

    const [searchParams, setSearchParams] = useSearchParams();
    const [routes, setRoutes] = useState<RouteDetails[]>([]);
    const [displayDir, setDisplayDir] = useState(false);
    const [selectedRoute, setSelectedRoute] = useState<RouteDetails>();

    const source = searchParams.get('source') as string;
    const destination = searchParams.get('destination') as string;

    function importAll(r: any) {
      let finalDict = {} as Object
      const keys = r.keys()
      const values = r.keys().map(r)
      
      for (let i=0; i <keys.length; i++){
          const key = keys[i].split("/")[1]
          if (key !== undefined){
              finalDict[key.split('.')[0]] = values[i]
          }
      }

      return finalDict;
  }
  const roads = importAll(require.context('../../data/roads/', true, /\.(png|jpe?g|svg)$/));
  
  return (
    <>
        { !displayDir ? 
        // if dw display yet den show all results
        <div className='tw-flex tw-justify-center tw-p-10'>
        <div className='tw-flex-1'>
        <Form source={source} destination={destination} setRoutes={setRoutes}/>
        </div>
        <div className='tw-flex-1 tw-pl-10'>
          <>
          <h1>Retrieveing Your Best Routes...</h1>
            {
              // routes.length !== 0 && (
                routes.map((route, index) => {
                  return(
                    <RoutesBox route={route} setDisplayDir={setDisplayDir} setSelectedRoute={setSelectedRoute}/>
                  )
                })
              // )
            }
          </>
        </div>
        </div>
        :
        // display one result map view
        <div className='tw-flex tw-h-screen tw-w-screen'>
        <div className="tw-shadow tw-p-4 tw-w-[20%]">
            <button onClick={(() => setDisplayDir(false))}>&#60; Back</button>
            <h1 className="tw-pt-8">Map View</h1>
            <p>From {source} to {destination}.</p>
            <p className='tw-font-bold tw-text-xl'>Option {selectedRoute?.option}</p>
            <p className='tw-font-bold tw-text-lg'>{selectedRoute?.timeStart}: {selectedRoute?.timeEnd}</p>
            <p className='tw-font-bold tw-text-lg'>Roads to Pass:</p>
            {selectedRoute?.route.map((road) => 
            <p>{road}</p>
            )}
        </div>
        <div className='tw-shadow tw-w-[80%]'>
          <div className='tw-relative tw-w-full tw-h-screen'>
            <img src={map} alt='map' className='tw-h-screen tw-w-full tw-overflow-scroll tw-absolute tw-top-0 tw-right-0'/>
            {selectedRoute?.route[0].map((road, index) => {
              return <img src={roads[road]} alt='road' className='tw-h-screen tw-w-full tw-overflow-scroll tw-absolute tw-top-0 tw-right-0'/>
            })}

            <p>{selectedRoute?.route}</p>

          </div>
        </div>
    </div>}
      </>
  );
}

export default GetRoute;