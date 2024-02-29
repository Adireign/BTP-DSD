import React from 'react'
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { useState } from 'react';
import UpperNav from './UpperNav';
import QuizForm from './Form';
import { useEffect } from 'react';
import Loading from './Loading';

const clientId = '1099148463228-fniq392tv0qv5hlbm084r9m8tp8ph0ls.apps.googleusercontent.com';
const Firstpage = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false)
    const [loggedInName, setLoggedInName] = useState('')
    const [loggedInEmail, setLoggedInEmail] = useState('')
    const [loading, setLoading] = useState(true)

    const onSuccessLogin = (res) => {
        console.log("Login Success current user:")
        const { name, email } = res.profileObj
        console.log("name: ", name)
        console.log("email", email)
        setLoggedInEmail(email)
        setLoggedInName(name)
        setIsLoggedIn(true)
    }
    const onFailureLogin = (res) => {
        console.log("Login failed", res)
    }
    const onSuccessLogout = () => {
        console.log("logout done")
        setIsLoggedIn(false)
        setLoggedInEmail('')
        setLoggedInName('')
    }
    useEffect(() => {
        // Simulate loading delay (you can replace this with your actual data loading logic)
        setTimeout(() => {
            setLoading(false);
        }, 2000);
    }, []);
    return (
        <div>
            {
                loading ?
                    <Loading /> :
                    <>
                        <div className="App">
                            {isLoggedIn ? (
                                <div>
                                    {/* Content for authenticated users */}
                                    <UpperNav name={loggedInName} email={loggedInEmail} />
                                    <div className='relative isolate px-60 lg:px-8'>
                                        <div class="mt-5">
                                            <div class="hidden sm:flex sm:justify-center">
                                                <div class=" px-3 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
                                                    <GoogleLogout
                                                        clientId={clientId}
                                                        buttonText="Logout"
                                                        onLogoutSuccess={onSuccessLogout}
                                                    />

                                                </div>
                                                <div class=" px-3 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
                                                    <GoogleLogin
                                                        clientId={clientId}
                                                        buttonText="Sign in using other account"
                                                        onSuccess={onSuccessLogin}
                                                        onFailure={onFailureLogin}
                                                        cookiePolicy={'single_host_origin'}
                                                        isSignedIn={true}
                                                    />

                                                </div>

                                            </div>
                                        </div>
                                    </div>
                                    <QuizForm />
                                </div>
                            ) : (
                                <div class="bg-white py-24 sm:py-32">
                                    <div class="mx-auto max-w-7xl px-6 lg:px-8">
                                        <div class="mx-auto max-w-2xl lg:text-center">
                                            <h2 class="text-base font-semibold leading-7 text-indigo-600"><GoogleLogin
                                                clientId={clientId}
                                                buttonText="Sign in with Google"
                                                onSuccess={onSuccessLogin}
                                                onFailure={onFailureLogin}
                                                cookiePolicy={'single_host_origin'}
                                                isSignedIn={true}
                                            /></h2>
                                            <p class="mt-4 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Attempt Your personalized quiz and assess yourself</p>
                                            <p class="mt-6 text-lg leading-8 text-gray-600">Sign in using any of your google account to generate quiz. You can also start an assessment and generate your marks.</p>
                                        </div>
                                    </div>
                                </div>

                            )}
                        </div>
                    </>
            }
        </div>
    )
}

export default Firstpage
