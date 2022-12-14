import Sidebar from '../../components/sidebar';
import { useState, useEffect } from 'react'
import { RouteDetails } from '../routesBox';
import { requestRoute } from '../../pages/route';

interface IProps {
    source: string,
    destination: string,
    setRoutes: React.Dispatch<React.SetStateAction<RouteDetails[]>>,
    setSelectDetails: React.Dispatch<React.SetStateAction<requestRoute | undefined>>,
    selectDetails: requestRoute | undefined,
}

const API = process.env.REACT_APP_API_ENDPOINT

function Form({ source, destination, setRoutes, setSelectDetails, selectDetails }: IProps) {

    const [currentSource, setCurrentSource] = useState(source);
    const [currentDestination, setCurrentDestination] = useState(destination);
    const [currentDateTime, setCurrentDateTime] = useState("");
    const [errorMsg, setErrorMsg] = useState("");

    
    useEffect(() => {
        if (selectDetails !== undefined) {
            setCurrentSource(selectDetails.source);
            setCurrentDestination(selectDetails.destination);
            setCurrentDateTime(selectDetails.datetime);
        }
      }, [selectDetails]);


    const getOutput = async () => {

        if (!currentSource || !currentDestination || !currentDateTime) {
            return setErrorMsg("Please fill all the fields");
        }

        setErrorMsg("");
        setSelectDetails({ source: currentSource, destination: currentDestination, datetime: currentDateTime });

        fetch(API + '/api/predict', {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              "source": currentSource,
              "destination": currentDestination,
              "datetime": currentDateTime
          })
          }).then(res => res.json())
          .then(res => {
            console.log(res)
            setRoutes([]);
    
            for (let i = 0; i < res.length; i++) {
              const route = res[i].route

              for (let j = 0; j < route.length; j++) {
                if ( route[j] % 2 === 0){
                  // if its an even number, minus 1
                  route[j] = route[j] - 1
                }
              }
                
              // }
              setRoutes(routes => [...routes, 
                {
                  "option": res[i].option,
                  "route": res[i].route,
                  "timeStart": res[i].timeStart,
                  "timeEnd": res[i].timeEnd,
                  "destination": res[i].destination,
                  "source": res[i].source,
                  "timeNeeded": Math.round(res[i].timeNeeded),
                  "delay": res[i].delay === 0 ? false : true,
                  "delayTime": res[i].delayTime,
                }
              ]);
            }
            
          });
        
      }

    return (
        <>
            <div className='tw-flex'>
                <div className='tw-pt-0'>
                <h1>One Last Thing! When are you leaving Port {currentSource}?</h1>
                    <div className='tw-flex'>
                    <div>
                    <p className="tw-mt-4">Where are you now?</p>
                    <input
                        type="text"
                        defaultValue={currentSource}
                        onChange={(e) => setCurrentSource(e.target.value)}
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                    />
                    </div>
                    <div className='tw-ml-2'>
                    <p className="tw-mt-4">Where are you heading?</p>
                    <input
                        type="text"
                        defaultValue={currentDestination}
                        onChange={(e) => setCurrentDestination(e.target.value)}
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                    />
                    </div>
                    </div>
                    <p className="tw-mt-4">When are you departing?</p>
                    <input
                        type="datetime-local"
                        defaultValue={currentDateTime}
                        placeholder="Date and Time of Departure"
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                        onChange={(e) => setCurrentDateTime(e.target.value)}
                    />
                    <button 
                    className="tw-mt-4 tw-w-full tw-p-2 tw-bg-primary tw-text-white tw-rounded-md hover:tw-bg-primaryDark"
                    onClick={(() => getOutput())}>Get Route</button>
                    <p className='tw-text-red-600'>{errorMsg}</p>
                </div>
                
            </div>
        </>
    );
}

export default Form;