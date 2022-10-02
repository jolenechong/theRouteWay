import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import Form from '../../components/form';
import RoutesBox, { RouteDetails } from '../../components/routesBox';
// @ts-ignore
import map from '../../data/map.png';

interface Object {
  [key: string]: string;
}

export interface requestRoute {
  source: string,
  destination: string,
  datetime: string,
}

function GetRoute() {

  const navigate = useNavigate();

    const [searchParams, setSearchParams] = useSearchParams();
    const [routes, setRoutes] = useState<RouteDetails[]>([]);
    const [displayDir, setDisplayDir] = useState(false);
    const [selectedRoute, setSelectedRoute] = useState<RouteDetails>();
    const [selectDetails, setSelectDetails] = useState<requestRoute>(); // these is the info given

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
  
  const roads = importAll(require.context('../../data/roads', false, /\.(png|jpe?g|svg)$/));
  
  return (
    <>
        { !displayDir ? 
        // if dw display yet den show all results
        <div className='tw-flex tw-justify-center tw-p-10'>
        <div className='tw-flex-1'>
        <button onClick={(() => navigate(-1))}>&#60; Back</button>
        <Form source={source} destination={destination} setRoutes={setRoutes} selectDetails={selectDetails} setSelectDetails={setSelectDetails}/>
        </div>
        <div className='tw-flex-1 tw-pl-10'>
          <>
          <h1 className='tw-pt-10'>Your Best Routes</h1>
          <p className='tw-pb-2'>Pick a Departure Date and Time and explore your options!</p>
            {
              // routes.length !== 0 && (
                (routes.length == 0 && selectDetails != null) && (
                  <>
                  <h1>Retrieving Your Best Routes...</h1>
                  <div className='tw-rounded-xl tw-bg-blue-100 tw-p-6 tw-relative tw-mt-2'>
                    <div className='tw-animate-pulse'>
                        <div className="tw-bg-gray-400 tw-w-54 tw-h-4 tw-rounded-lg"></div>
                        <div className="tw-my-2"></div>
                        <div className="tw-bg-gray-400 tw-w-40 tw-h-4 tw-rounded-lg"></div>
                        <div className="tw-my-2"></div>
                        <div className="tw-bg-gray-400 tw-w-48 tw-h-4 tw-rounded-lg"></div>
                  </div>
                    </div>
                    </>
                )
          }{
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
            <p className='tw-font-semibold tw-pt-6'>Option {selectedRoute?.option}</p>
            <p className='tw-font-semibold tw-text-lg'>{selectedRoute?.timeStart}: {selectedRoute?.timeEnd}</p>
            <p className='tw-font-semibold tw-pt-4'>Roads to Pass:</p>
            {selectedRoute?.route.map((road) => 
               <p>Road {road}</p>
            )}
        </div>
        <div className='tw-shadow tw-w-[80%]'>
          <div className='tw-relative tw-w-full tw-h-screen'>
            <img src={map} alt='map' className='tw-h-screen tw-w-full tw-overflow-scroll tw-absolute tw-top-0 tw-right-0'/>
            {selectedRoute?.route.map((road, index) => {
              return <img src={roads[road]} alt={`road ${road}`} className='tw-h-screen tw-w-full tw-overflow-scroll tw-absolute tw-top-0 tw-right-0'/>
            })}

            <p>{selectedRoute?.route}</p>

          </div>
        </div>
    </div>}
      </>
  );
}

export default GetRoute;