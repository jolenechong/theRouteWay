import { useEffect, useState } from 'react';

export interface RouteDetails {
    option: number,
    route: Array<Array<number>>, // your nested array routes here
    timeStart: string,
    timeEnd: string,
    destination: string,
    source: string,
    timeNeeded: number,
    delay: Boolean,
    delayTime?: number, //optional
}

interface IProps {
    route: RouteDetails,
    setDisplayDir: React.Dispatch<React.SetStateAction<boolean>>,
    setSelectedRoute: React.Dispatch<React.SetStateAction<RouteDetails | undefined>>,
}

function RoutesBox({ route, setDisplayDir, setSelectedRoute }: IProps) {

    return (
        <>
            <div className='tw-rounded-xl tw-bg-blue-100 tw-p-6 tw-relative tw-mt-2'>
                <p>Option {route.option}</p>
                <p className='tw-font-bold tw-text-lg'>{route.timeStart} -  {route.timeEnd}</p>
                <p>from {route.source}</p>

                <div className='tw-absolute tw-top-6 tw-right-6'>
                    <p className='tw-text-right'>{route.timeNeeded} min</p>
                    {route.delay && <p className='tw-text-red-600'>additional {route.delayTime} min delay</p>}
                </div>
                {route.delay ? <p className='tw-text-red-600'>*Potential Delays due to Traffic Jams</p> : <></>}
                <button className='tw-underline tw-outline-none tw-bg-none tw-absolute tw-bottom-6 tw-right-6' onClick={(() => {
                    setDisplayDir(true)
                    setSelectedRoute(route)
                })}>Get Directions</button>
            </div>
        </>
    );
}

export default RoutesBox;