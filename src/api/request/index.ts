import request from '@/axios'
import { RequestResponse } from './types'

export const request1 = () => {
  return request.get<IResponse<RequestResponse>>({
    url: '/api/request/1'
  })
}

export const request2 = () => {
  return request.get<IResponse<RequestResponse>>({
    url: '/api/request/2'
  })
}

export const request3 = () => {
  return request.get<IResponse<RequestResponse>>({
    url: '/api/request/3'
  })
}

export const request4 = () => {
  return request.get<IResponse<RequestResponse>>({
    url: '/api/request/4'
  })
}

export const request5 = () => {
  return request.get<IResponse<RequestResponse>>({
    url: '/api/request/5'
  })
}

export const expired = () => {
  return request.get<IResponse<RequestResponse>>({
    url: '/api/request/expired'
  })
}
