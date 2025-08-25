import request from '@/axios'
import type { WorkplaceTotal, Project, Dynamic, Team, RadarData } from './types'

export const getCountApi = (): Promise<IResponse<WorkplaceTotal>> => {
  return request.get({ url: '/api/workplace/total' })
}

export const getProjectApi = (): Promise<IResponse<Project>> => {
  return request.get({ url: '/api/workplace/project' })
}

export const getDynamicApi = (): Promise<IResponse<Dynamic[]>> => {
  return request.get({ url: '/api/workplace/dynamic' })
}

export const getTeamApi = (): Promise<IResponse<Team[]>> => {
  return request.get({ url: '/api/workplace/team' })
}

export const getRadarApi = (): Promise<IResponse<RadarData[]>> => {
  return request.get({ url: '/api/workplace/radar' })
}
