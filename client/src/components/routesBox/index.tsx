import { useEffect, useState } from 'react';

interface IProps {
    option: number,
    route: Array<Array<number>>, // your nested array routes here
    timeStart: string,
    timeEnd: string,
    destination: string,
    source: string,
    timeNeeded: number,
    delay: Boolean,
    delayTime?: number, //optional
    setDisplayDir: React.Dispatch<React.SetStateAction<boolean>>
}

function RoutesBox({ option, route, timeStart, timeEnd, destination, source, timeNeeded, delay, delayTime, setDisplayDir }: IProps) {

    return (
        <>
            <>
                        <div className='tw-rounded-xl tw-bg-blue-100 tw-p-6 tw-relative tw-mt-2'>
                            <p>Option {option}</p>
                            <p className='tw-font-bold tw-text-lg'>{timeStart}: {timeEnd}</p>
                            <p>from {source}</p>

                            <div className='tw-absolute tw-top-6 tw-right-6'>
                                <p className='tw-text-right'>{timeNeeded} min</p>
                                {delay && <p className='tw-text-red-600'>additional {delayTime} min delay</p>}
                            </div>
                            {delay ? <p className='tw-text-red-600'>*Potential Delays due to Traffic Jams</p> : <></>}
                            <button className='tw-underline tw-outline-none tw-bg-none tw-absolute tw-bottom-6 tw-right-6' onClick={(() => setDisplayDir(true))}>Get Directions</button>
                        </div>

            </>
        </>
    );
}

export default RoutesBox;