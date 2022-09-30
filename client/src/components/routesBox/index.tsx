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
}

function RoutesBox({ option, route, timeStart, timeEnd, destination, source, timeNeeded, delay, delayTime }: IProps) {

    const [displayDir, setDisplayDir] = useState(false);

    const handleClick = () => {

    }

    return (
        <>
            <>
                {
                    displayDir ?
                        <div>
                            <div className="tw-shadow tw-p-4">
                                <h1 className="tw-pt-8">Map View</h1>
                                <p>From {source} to {destination}.</p>
                                <p className='tw-font-bold tw-text-xl'>Option {option}</p>
                                <p className='tw-font-bold tw-text-lg'>{timeStart}: {timeEnd}</p>
                                <p className='tw-font-bold tw-text-lg'>Roads to Pass:</p>
                                {route.map((road, index) => {
                                    return <p key={index}>{road}</p>
                                })}


                            </div>
                            <div className='tw-shadow tw-w-[70%] tw-p-4'>
                            </div>
                        </div>
                        :
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
                }


            </>
        </>
    );
}

export default RoutesBox;